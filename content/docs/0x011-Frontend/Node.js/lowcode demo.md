
Review
1. 2024-08-17 18:45

> [!Summary]
> 

## 一、Introduction

```js
if (process.env.IS_PUBLISH_LOWCODE === 'N') process.exit()

const fs = require('fs')
const path = require('path')
const axios = require('axios')
const crypto = require('crypto')
const { execSync } = require('child_process')

const isLocal = !process.env.AWP_DEPLOY_ENV
isLocal && require('./env')

const { env } = process

let reactParser
try {
  reactParser = require('@rome/react-parser')
} catch {
  console.warn('未安装@rome/react-parser，跳过低代码发布')
  process.exit(231)
}

function generateBAString(uri, method, clientId, clientSecret) {
  // 获取http时间
  const timeSpan = new Date().toUTCString()
  const stringToSign = `${method.toUpperCase()} ${uri}\n${timeSpan}`
  const signature = crypto
    .createHmac('sha1', clientSecret)
    .update(stringToSign)
    .digest()
    .toString('base64')
  const Authorization = `${'MWS '}${clientId}:${signature}`
  return {
    Date: timeSpan,
    Authorization,
  }
}

const axPost = (pathname, params, options = {}) => {
  const headers = generateBAString(pathname, 'POST', env.TAM_CLIENT_ID, env.TAM_CLIENT_SECRET)

  console.log('headers ===>', headers)
  console.log('params ===>', JSON.stringify(params))

  return axios.post(pathname, params, {
    baseURL:
      env.TAM_API_ENV === 'test'
        ? 'http://harbour.dzu.test.sankuai.com'
        : 'https://harbour.sankuai.com',
    headers,
    ...options,
  })
}

/**
 * 获取低代码Meta配置对象
 * @param {String} dirPath: 组件目录地址，相对或绝对路径
 * @param {String} pkgName: 组件包名，如 @corn/block-demo1
 */
function getAssetsInfo(dirPath, pkgName) {
  const assetPath = path.resolve(dirPath, './build/assets.json')
  let lowcodePkg
  let assetsObj
  let metaJson = ''
  if (fs.existsSync(assetPath)) {
    try {
      const assetContent = fs.readFileSync(assetPath, 'utf8') || ''
      assetsObj = JSON.parse(assetContent) || {}
      if (assetsObj && assetsObj.packages && assetsObj.packages.length > 0) {
        lowcodePkg = assetsObj.packages.find(d => d.package === pkgName) || {}
      }
    } catch (e) {
      console.log('assetPath', assetPath)
      console.error('[readFileSync error]', e)
      assetsObj = {}
      lowcodePkg = {}
    }
  } else {
    console.log(`组件meta文件不存在, 文件路径：${assetPath}`)
  }
  try {
    metaJson = JSON.stringify((assetsObj.components || [])[0] || {})
  } catch (e) {
    console.error('[assetsObj stringify error]', e)
    console.log('assetsObj', assetsObj)
    console.log('assetsObj.components', assetsObj.components)
  }

  return {
    metaJson,
    packages: assetsObj.packages || [], // 依赖的资源
    umdUrl: lowcodePkg.urls || lowcodePkg.editUrls || [], // 资产包资源链接，js和css各一份 ['xxxxx.umd.js', 'xxxx.umd.css']
  }
}

/**
 * 获取build.lowcode.js配置文件
 * @param {String} dirPath: 组件目录地址，相对或绝对路径
 */
function getLowcodeEntry(dirPath) {
  const filePath = './build.lowcode.js'
  let entryPath = ''
  try {
    const childConfPath = path.resolve(dirPath, filePath)
    const useChild = fs.existsSync(childConfPath)
    const { plugins } = useChild ? require(childConfPath) : require(path.resolve(filePath))
    const confObj =
      ((plugins || []).find(d => d[0] === '@alifd/build-plugin-lowcode') || plugins[0] || [])[1] || {}
    entryPath = confObj.entryPath || ''
    if (useChild && entryPath) entryPath = path.join(dirPath, entryPath)
  } catch (e) {
    console.error('读取 build.lowcode.js 文件失败', e)
  }
  return entryPath
}

/**
 * 发布至Component平台
 * @param {String} dirPath: 组件目录地址，相对或绝对路径
 */
function publishToComponent(dirPath) {
  if (!env.CMP_PKG_ID || !env.CMP_USER_TOKEN) return
  let ssMetaTool
  try {
    ssMetaTool = require('@ss/meta-tool/dist/index')
  } catch {
    console.warn('未安装@ss/meta-tool/dist/index，跳过发布至Component平台')
    process.exitCode = 231
    return
  }
  try {
    const assetPath = path.resolve(dirPath, './build/assets.json')
    const assetContent = fs.readFileSync(assetPath, 'utf8') || ''
    if (fs.existsSync(assetPath)) {
      const assetsObj = JSON.parse(assetContent) || {}
      assetsObj.packages && assetsObj.packages.unshift(...[
        {
          "package": "lodash",
          "library": "_",
          "urls": [
            "https://g.alicdn.com/platform/c/lodash/4.6.1/lodash.min.js"
          ]
        },
        {
          "title": "react",
          "package": "react",
          "type": "procode",
          "version": "16.13.1",
          "library": "react",
          "urls": [
            "https://unpkg.com/react@16.13.1/umd/react.production.min.js"
          ]
        },
        {
          "title": "react-dom",
          "package": "react-dom",
          "type": "procode",
          "version": "16.13.1",
          "library": "react-dom",
          "urls": [
            "https://unpkg.com/react-dom@16.13.1/umd/react-dom.production.min.js"
          ]
        }
      ])
      const newAssetPath = path.resolve(assetPath, '../assets_cmp.json')
      fs.writeFileSync(newAssetPath, JSON.stringify(assetsObj, null, 2))
      ssMetaTool.uploadAndUpdateAsset({
        token: env.CMP_USER_TOKEN,
        path: path.relative('./', newAssetPath),
        id: env.CMP_PKG_ID,
        // PS: Component平台正式环境值为 prod
        env: env.TAM_API_ENV === 'production' ? 'prod' : env.TAM_API_ENV,
      })
    }
  } catch (e) {
    console.warn('发布至Component平台失败', e)
    process.exitCode = 231
  }
}

async function start() {
  if (!env.projectRoot) {
    console.log('未配置环境变量 projectRoot，使用缺省值 ./\n')
    Object.assign(env, {
      projectRoot: './',
    })
  }
  if (!fs.existsSync(path.resolve(env.projectRoot, 'lowcode'))) {
    console.log('不存在 lowcode 文件夹，不发布低代码物料')
    process.exit(231)
  }

  try {
    const cornConfPath = env.CORN_CONF_PATH
    execSync(
      `node_modules/.bin/corn-lowcode build${cornConfPath ? ` -c ${cornConfPath}` : ''}`,
      { stdio: 'inherit' }
    )
  } catch (e) {
    console.error('[execSync error]', e)
    process.exit(1)
  }

  try {
    const compsRelDir = env.projectRoot || './'
    const packObj = require(path.resolve(compsRelDir, './package.json')) || {}
    const compName = (packObj.name || '').replace(/^[^/]+\//, '')
    const { packages, metaJson, umdUrl } = getAssetsInfo(compsRelDir, packObj.name)

    await axPost('/api/tam/paas/setPackages', {
      projectGit: env.AWP_GIT_REPO,
      packages: [
        {
          dirPath: compsRelDir, // 资产包入口路径，以 './' 开头
          name: compName,
          npm: packObj.name,
          version: packObj.version, // 资产包版本号
          versionType: env.AWP_DEPLOY_ENV === 'production' ? 'prod' : 'beta', // 版本类型，beta、prod
          assetType: 'react-component', // 资产类型，枚举:'vue-component', 'react-component', 'setter'等
          umdUrl,
          packages, // 依赖的资源
        },
      ],
    }).then(resp => {
      console.log('----------------------------')
      console.log('setPackages ===>', JSON.stringify(resp.data))
      console.log('----------------------------')
    })

    if (env.TAM_PKG_TAG) {
      await axPost(`/api/tam/paas/ba/setPackageTag`, {
        projectGit: env.AWP_GIT_REPO,
        npm: packObj.name,
        tagIds: env.TAM_PKG_TAG,
        isCover: env.IS_TAG_OVERWRITE || '0',
      })
        .then(resp => {
          console.log('----------------------------')
          console.log('setPackageTag ===>', JSON.stringify(resp.data))
          console.log('----------------------------')
        })
        .catch(e => {
          console.warn('setPackageTag失败 ===>', e)
          process.exitCode = 231
        })
    }

    const entryPath = getLowcodeEntry(compsRelDir)
    const tmpResult = reactParser({
      cwd: process.cwd(),
      projectType: 'Rome-Component',
      projectRoot: compsRelDir,
      ...(entryPath ? { entryPath } : {}),
    })
    // if (isLocal) {
    //   const tmpFilePath = path.resolve(__dirname, './tmpResult.json')
    //   fs.writeFileSync(tmpFilePath, JSON.stringify(tmpResult))
    // }

    const tmpPkg = (tmpResult.packages || [])[0] || {}
    const tamCmps = (tmpPkg.assets && tmpPkg.assets.components) || []
    // metaJson检测是否存在
    if (tamCmps[0] && !tamCmps[0].metaJson) {
      console.log('metaJson不存在, 需要赋值')
      tamCmps[0].metaJson = metaJson
    }

    await axPost('/api/tam/paas/setComponents', {
      projectGit: env.AWP_GIT_REPO,
      packageDirPath: compsRelDir,
      version: packObj.version || '',
      assetType: 'react-component',
      tag: env.AWP_DEPLOY_ENV === 'production' ? 'latest' : 'beta',
      components: tmpResult.packages,
    }).then(resp => {
      console.log('----------------------------')
      console.log('setComponents ===>', JSON.stringify(resp.data))
      console.log('----------------------------')
    })

    publishToComponent(compsRelDir)
  } catch (e) {
    console.error(e)
    process.exit(1)
  }
}

start()

```


## Reference


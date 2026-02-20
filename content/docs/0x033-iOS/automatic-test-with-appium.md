---
weight: 10
bookFlatSection: false
bookCollapseSection: true
title: Automatic Test with Appium
Created: 2026-02-14
Last updated: 2026-02-14
tags:
  - iOS
  - AutomatedTesting
---
## iOS 自动化测试环境安装与配置

**相关资料**
- Appium <https://appium.io/docs/en/latest/> 
- Appium Github https://github.com/appium/appium
- Appium Inspector <https://github.com/appium/appium-inspector> 
- WebDriverAgent <https://appium.github.io/appium-xcuitest-driver/4.16/wda-custom-server/>
- Appium 中文网站 <https://appium.io/docs/zh/latest/intro/>
- Appium XCUITest Driver <https://appium.github.io/appium-xcuitest-driver/latest/overview/> 

### 前置条件

1. 配置 NodeJS 环境，要求版本 ≥ 20
2. 配置 Java 环境，如安装 `openjdk@17`
3. 下载安装 Xcode，并安装命令行工具：`xcode-select --install`
4. iOS 真机配置：开启开发者模式、连接 macOS 电脑并信任；在 **设置 → 开发者 → Enable UI Automation** 中开启 UI 自动化。真机 UDID 可在连接后通过 Xcode **Window → Devices and Simulators** 或终端 `idevice_id -l`（需安装 `libimobiledevice`）查看。


### Appium 安装配置

```sh
npm install -g appium
```


安装 iOS 驱动：

```sh
appium driver install xcuitest
```


验证环境安装：

```sh
npm install -g appium-doctor
appium-doctor --ios
```

#### 配置 WebDriverAgent (WDA)
> WDA 是 Appium 在 iOS 设备上执行操作的中转站，必须经过 Apple 签名才能在真机上运行。

进入 WDA 目录：

```sh
cd "$HOME/.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent"
```

##### 编译与签名
1. 进入上述目录，打开 `open WebDriverAgent.xcodeproj`
2. 在 Xcode 的 **Targets** 中，依次选择 **WebDriverAgentLib** 和 **WebDriverAgentRunner**
3. 在 **Signing & Capabilities** 选项卡中：
    - 勾选 **Automatically manage signing**。
    - 在 **Team** 中选择你的 Apple ID 账号。
    - **Bundle Identifier**: 将默认的 `com.facebook.WebDriverAgentRunner` 修改为一个全球唯一的名称（如 `com.yourname.wda.runner`），否则会报错。

*Signing & Capabilities 配置示意*

![[Screenshot 2026-02-14 at 08.35.11.png]]


#### 配置 Appium Inspector
这是一个 UI 可视化工具，可以帮你录制脚本和查看元素树。
- [下载 Appium Inspector](https://github.com/appium/appium-inspector/releases)
- 输入 Capabilities（Caps），点击 **Start Session**。其中 `udid` 为设备唯一标识，`derivedDataPath` 需与后续命令行构建 WDA 时一致，便于复用已构建的 WDA。

参考（真机测试系统计算器，请按实际设备替换 `udid` 与 `deviceName`）：

```json
{
  "platformName": "iOS",
  "appium:udid": "00008101-001970D20C29001E",
  "appium:bundleId": "com.apple.calculator",
  "appium:automationName": "XCUITest",
  "appium:noReset": true,
  "appium:usePrebuiltWDA": true,
  "appium:deviceName": "MyiPhone12",
  "appium:derivedDataPath": "~/Downloads/appium_wda_ios"
}
```

*Appium Inspector 中填写 Caps 并 Start Session*

![[Screenshot 2026-02-14 at 09.05.24.png]]

#### 运行 Appium 服务

```sh
appium
```

在 Inspector 中点击 **Start Session** 即可连接设备并查看元素树。

*连接成功后的 Inspector 界面*

![[Screenshot 2026-02-14 at 09.10.18.png]]


#### 自动化测试
若不通过 Appium Inspector 发起会话，需要先在本机用命令行构建并安装 WDA 到真机（见下方命令）。

```sh
# 构建 Appium WDA
xcodebuild clean build-for-testing \
  -project ~/.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent/WebDriverAgent.xcodeproj \
  -derivedDataPath ~/Downloads/appium_wda_ios \
  -scheme WebDriverAgentRunner \
  -destination generic/platform=iOS \
  -allowProvisioningUpdates
```

**Python 示例脚本**（需先 `uv add appium-python-client`）：

```python
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# 配置参数
options = XCUITestOptions()
options.platform_name = 'iOS'
# options.platform_version = '26.2.1'  # 根据实际系统版本修改
options.device_name = 'iPhone 12'  # 模拟器名称

# 真机配置
options.udid = 'xxx'
# ⚠️ 重要：xcode_org_id 必须是 Team ID（10位字母数字），不是邮箱！
# 查看方法：Xcode -> Preferences -> Accounts -> 选择你的 Apple ID -> 查看 Team ID
# options.xcode_org_id = 'xxx'  # 请替换为你的 Team ID（例如：ABC123DEFG）
# options.xcode_signing_id = 'iPhone Developer'

# 调试配置：显示 Xcode 构建日志（帮助排查问题）
# options.show_xcode_log = True
# options.use_prebuilt_wda = False  # 强制重新构建 WDA

# 被测应用（二选一）
# 方式1：安装包路径（.app 或 .ipa）
# options.app = '/path/to/YourApp.app'
# 方式2：已安装应用的 Bundle ID
options.bundle_id = 'com.honeymorning.native.RNWithoutFrameworkDemo'
# options.bundle_id = 'com.apple.calculator'
options.no_reset = True
options.use_prebuilt_wda = True
options.derived_data_path = "~/Downloads/appium_wda_ios"

# 其他配置
options.wda_launch_timeout = 120000  # WDA 启动超时（毫秒）
options.wda_connection_timeout = 120000

# 连接 Appium（Appium 2 默认根路径为 `/`，不再使用 `/wd/hub`）
driver = webdriver.Remote('http://localhost:4723', options=options)

try:
  # 等待应用启动
  time.sleep(3)

  # 示例
  # 通过 XPath 查找
  input_field = driver.find_element(
      AppiumBy.XPATH,
      '//XCUIElementTypeTextField[@value="Enter the text you want to store"]')
  input_field.send_keys('testuser')

  save_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Save')
  save_button.click()

  # 滑动操作
  driver.swipe(200, 600, 200, 200, 1000)  # 从下到上滑动

  # 断言验证
  assert driver.find_element(
      AppiumBy.CLASS_NAME,
      'XCUIElementTypeTextField',
  ).is_displayed()
  print("测试通过！")

except Exception as e:
  print(f"测试失败: {e}")

finally:
  driver.quit()
```

### 常见问题

- **WDA 安装/启动失败**：确认设备已信任电脑、已开启 UI Automation；Bundle ID 已改为唯一值且与 Xcode 中一致；Team 与证书正确。
- **Session 无法创建**：先单独执行 `appium`，再运行脚本；真机时需填写正确的 `udid` 和（若需签名）`xcode_org_id`（Team ID）。
- **元素找不到**：用 Appium Inspector 确认选择器与当前页面一致；系统弹窗或权限框可能遮挡目标元素，需先处理弹窗。

### 参考资料

- [W3C WebDriver 规范](https://w3c.github.io/webdriver/)
- 文首「相关资料」中的 Appium / WDA / Inspector 官方文档

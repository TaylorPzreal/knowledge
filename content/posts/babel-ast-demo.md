---
title: "Babel Ast Demo"
date: 2023-08-25
tags: 
 - Babel
 - AST
categories: Frontend
# bookComments: false
# bookSearchExclude: false
---

# Babel AST Demo

Review
1. 2023/08/25


```js
const fs = require('fs');
const path = require('path');
const babel = require("@babel/core");
const { parse } = require('@babel/parser');
const traverse = require('@babel/traverse').default;

const srcFilePath = './src/main.js';

// Store source codes
const sourceCodes = {};

// Function to recursively process dependencies
function processDependency(filePath) {
  if (!sourceCodes[filePath]) {
    const sourceCode = fs.readFileSync(filePath, 'utf-8');
    sourceCodes[filePath] = sourceCode;

    // Parse the source code to extract import statements
    const ast = parse(sourceCode, {
      sourceType: 'module',
      plugins: ['jsx', 'typescript'], // Add plugins as needed
    });

    // Traverse the AST to find dependencies
    traverse(ast, {
      ImportDeclaration: ({ node }) => {
        const dependencyPath = node.source.value;
        const absoluteDependencyPath = path.resolve(path.dirname(filePath), dependencyPath);
        processDependency(absoluteDependencyPath);

        // Remove import declarations
        node.specifiers.forEach(specifier => {
          if (t.isImportSpecifier(specifier)) {
            const name = specifier.imported.name;
            const source = t.stringLiteral(dependencyPath);
            const importDeclaration = t.importDeclaration([specifier], source);
            const importIndex = ast.program.body.indexOf(node);
            ast.program.body.splice(importIndex, 1, importDeclaration);
          }
        });
      },
    });
  }
}

// Start processing the main file and its dependencies
processDependency(path.resolve(srcFilePath));

// Output the source codes
Object.entries(sourceCodes).forEach(([filePath, sourceCode]) => {
  console.log(`Source code for file: ${filePath}`);
  console.log(sourceCode);

  const { code } = babel.transform(sourceCode, {})
  console.log('\n--------------------------------------------\n');
  console.log(code);

});


// const data = require('./dist/bundle');
// babel.transformSync(data, { s });
```

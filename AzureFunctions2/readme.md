# Azure Functions
These are my notes from playing around with Azure Functions, following a [tutorial for VS Code](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python)

## Requirements
Easy-peasy usage of Azure Functions against VS Code with the [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)

# Environmental Variables
Azure Functions supports Application Settings which become Env Vars for Python, see [documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#environment-variables).

```
import os
test_value = os.environ['TestKey']
```
# Python via Docker
Remote development setup in VS Code to run via containers, see [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers) for details.  
Requires local installation of VS Code and Docker.

# End-user instructions
See `Instructions.pdf` for instructions on how to open the folder with VS Code, how to get VS Code to open in a container, etc.

# Container configuration
If end-users are going to be success, it needs to be as easy to use as possible.  
Make sure that the necessary extensions are added in the container, that the required environmental variables are loaded in correctly, and that the necessary local extensions are offered as recommendations.

## Environmental variables
Environmental variables can be fed directly into the container via Docker.  
Add the environmental variable in `.devcontainer/devcontainer.json` as follows:
```
"containerEnv": {
    "myEnv":    "myEnvValue",
    "myEnv2":   "someOtherValue",
},
```

*This way it is possible to keep the normal `.env` file clean for end-user inputs.*

## Container extensions
Extensions can be installed directly in the container.  
Add the full extension name in `.devcontainer/devcontainer.json` as follows:
```
"extensions": [
    "ms-python.python"
]
```

## Local VS Code extensions
Local extensions can be recommended by VS Code (creates a pop-up to install them).  
Add the full extension name in `.vscode/extensions.json` as follows:
```
"recommendations": [
    "ms-vscode-remote.remote-containers"
]
```
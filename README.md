```

░█▀▀█ ░█─░█ 　 ─█▀▀█ ░█▀▀█ ▀▀█▀▀ ▀█▀ ░█▀▀▀█ ░█▄─░█ ░█▀▀▀█ 　 ░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ ░█▀▀█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ 
░█─▄▄ ░█▀▀█ 　 ░█▄▄█ ░█─── ─░█── ░█─ ░█──░█ ░█░█░█ ─▀▀▀▄▄ 　 ─▀▀▀▄▄ ─░█── ░█▄▄█ ░█▄▄▀ ─░█── ░█▀▀▀ ░█▄▄▀ 
░█▄▄█ ░█─░█ 　 ░█─░█ ░█▄▄█ ─░█── ▄█▄ ░█▄▄▄█ ░█──▀█ ░█▄▄▄█ 　 ░█▄▄▄█ ─░█── ░█─░█ ░█─░█ ─░█── ░█▄▄▄ ░█─░█

```

*Starter template for your Github Action using Python and Docker.*




<p>


<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" />
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Github%20Actions-282a2e?style=for-the-badge&logo=githubactions&logoColor=367cfe"/>
</p>

# Getting Started


## Example Workflow

Path: `.github/workflows/example.yml`

```

name: Run py-docker gh-action

on:
  workflow_dispatch

jobs:
  run-action-job:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: run-docker-action
      id: run-docker-action
      uses: ./
      with:
        fname: 'data'

    - name: show-output
      run: |
        echo "Response Text: ${{ steps.run-docker-action.outputs.response-text }}"
    
```



# Folder Structure

```
|   action.yml
|   data.json
|   Dockerfile
|   LICENSE
|   main.py
|   README.md
|   requirements.txt
|
+---.github
|   \---workflows
|           example.yml

```


## License

    MIT

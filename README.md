[![Runs on Jupyter4NFDI](https://github.com/NFDI-Jupyter/ghactions/actions/workflows/notebooks.yaml/badge.svg)](https://hub.nfdi-jupyter.de/v2/gh/NFDI-Jupyter/ghactions/workingexample)


# Jupyter4NFDI GitHub Actions
  
[![Jupyter4NFDI](https://nfdi-jupyter.de/images/Jupyter4NFDI-top.png)](https://hub.nfdi-jupyter.de/)
  
This repository contains the currently supported Jupyter4NFDI GitHub Actions.

Add a Jupyter4NFDI badge to your GitHub README.md:  
```
[![Jupyter4NFDI approved](https://github.com/_repoowner_/_repotype_/actions/workflows/main.yml/badge.svg)](https://hub.nfdi-jupyter.de/v2/gh/_repoowner_/_repotype_/HEAD)
```  

Clicking on the Badge will launch your repository on Jupyter4NFDI.  

## Test notebooks
With this simple Action you can check if your repository and all notebooks inside are running on Jupyter4NFDI.  
1. Visit https://hub.nfdi-jupyter.de/hub/token , log in and create a token for the GitHub Action.
2. In your GitHub Repo browse to Settings -> Environments -> New Environment -> Name: jupyter4nfdi -> Add environment secret -> Secret Name: JUPYTERHUB_API_TOKEN, Value: token from first step
3. In your GitHub Repo browse to Actions -> "set up a workflow yourself" -> Copy the following text into it and click on "Commit changes" in the top right corner.
  
```
name: Runs on Jupyter4NFDI

on:
  workflow_dispatch:
  schedule:
    - cron: "0 7 * * 1"

jobs:
  notebooks:
    runs-on: ubuntu-latest
    environment: jupyter4nfdi
    steps:
      - name: Run notebooks via papermill on JupyterHub
        uses: NFDI-Jupyter/ghactions/.github/actions/notebooks@main
        with:
          repo: ${{ github.repository }}
          ref: ${{ github.ref_name }}
          # notebook_dirs: '["notebooks", "examples"]' # Only check specific folders in your repo
          token: ${{ secrets.JUPYTERHUB_API_TOKEN }}
```

That's it. Every monday at 7am all notebooks in your repository are executed on Jupyter4NFDI, to verify they're working as expected.  

### Successful Example
See logs [here](https://github.com/NFDI-Jupyter/ghactions/actions/runs/21878211862/job/63159807946)  
  
```
========== PAPERMILL LOGS ==========
{
  "exitCode": 0,
  "results": [
    {
      "notebook": "notebooks/index.ipynb",
      "exitCode": 0,
      "stdout": "Input Notebook:  notebooks/index.ipynb\nOutput Notebook: /tmp/tmp7s_dmcxb/index.ipynb\n\nExecuting:   0%|          | 0/9 [00:00<?, ?cell/s]Executing notebook with kernel: python3\n\nExecuting:  11%|\u2588         | 1/9 [00:01<00:11,  1.49s/cell]\nExecuting:  44%|\u2588\u2588\u2588\u2588\u258d     | 4/9 [00:04<00:05,  1.01s/cell]\nExecuting:  89%|\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2589 | 8/9 [00:04<00:00,  2.30cell/s]\nExecuting: 100%|\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588| 9/9 [00:04<00:00,  2.53cell/s]\nExecuting: 100%|\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588| 9/9 [00:05<00:00,  1.78cell/s]\n"
    }
  ]
}
===================================
Papermill job completed successfully
```

### Failed Example
See logs [here](https://github.com/NFDI-Jupyter/ghactions/actions/runs/21878348028/job/63158730655)  
  
```
========== PAPERMILL LOGS ==========
{
  "exitCode": 1,
  "results": [
    {
      "notebook": "/home/jovyan/index.ipynb",
      "exitCode": 1,
      "stdout": ...,
    }
  ]
}
===================================
Papermill job failed (exitCode=1)
Error: Input Notebook:  /home/jovyan/index.ipynb
Output Notebook: /tmp/tmpg1gskghl/index.ipynb
...

ModuleNotFoundError: No module named 'matplotlib'


Error: Process completed with exit code 1.
```

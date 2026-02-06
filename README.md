![Runs on Jupyter4NFDI](https://github.com/NFDI-Jupyter/ghactions/actions/workflows/notebooks.yaml/badge.svg) [![NFDI](https://nfdi-jupyter.de/images/nfdi_badge.svg)](https://hub.nfdi-jupyter.de/v2/gh/NFDI-Jupyter/ghactions/HEAD)

# Jupyter4NFDI GitHub Actions
  
[![Jupyter4NFDI](https://nfdi-jupyter.de/images/Jupyter4NFDI-top.png)](https://hub.nfdi-jupyter.de/)
  
This repository contains the currently supported Jupyter4NFDI GitHub Actions.

Add Jupyter4NFDI badges to your GitHub README.md:  
```
![Jupyter4NFDI approved](https://github.com/_repoowner_/_repotype_/actions/workflows/main.yml/badge.svg)
[![NFDI](https://nfdi-jupyter.de/images/nfdi_badge.svg)](https://hub.nfdi-jupyter.de/v2/gh/_repoowner_/_repotype_/_ref_)
```  
  
## Test notebooks
With this simple Action you can check if your repository and all notebooks inside are running on Jupyter4NFDI.  
1. Visit https://hub.nfdi-jupyter.de/hub/token , Log in and create a token for the GitHub Action.
2. In your GitHub Repo browse to Settings -> Environments -> New Environment -> Name: jupyter4nfdi -> Add environment secret -> Secret Name: JUPYTERHUB_API_TOKEN, Value: token from first step
3. In your GitHub Repo browse to Actions -> "set up a workflow yourself" -> Copy this text into it:
  
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

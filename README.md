# About this repo
Template file and folder structure for data pipelines written in python and Jupyter notebooks

## Acknowledgements
The repo is inspired by the 
[The Good Research Code Handbook](https://goodresearch.dev/setup#)
by Patick Mineault,
which is a fantastic resource for coding in academic research.

## Workflows and code
The workflows are stored as Jupyter notebooks in the [`notebooks`](./notebooks) directory.
The backend code is stored in the [`src`](./src) directory.
After following the installation instructions,
the code can be used via `from src import ...`,
as is done in [`example_workflow.ipynb`](./notebooks/example_workflow.ipynb).

# Installation
The following setup will
- create a `conda` environment with the packages defined in the [`environment.yml`](./environment.yml) file
- install the code in the `src` directory as a local python module via `pip`

## Prerequisites
### conda/mamba
Download and install [miniforge](https://github.com/conda-forge/miniforge), 
which gives you a light-weight `conda` installation and access to the
faster `mamba` package manager.
This is recommended if you do _not_ have Anaconda already installed.
Otherwise, just use [Anaconda](https://www.anaconda.com/download).
How to work with `conda` environments is explained in the 
[`mamba`](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#)
or 
[`conda`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
user guides.

### Git
Download and install [`git`](https://git-scm.com/downloads) version control.
`git` is the recommended way to acquire and update the code, but you can also manually download this repo.

## Installing local code
Getting the code up and running on a new system is done via the command in the `conda` prompt (adapt URL and name to your repo):
```
# get source code
git clone https://github.com/nspiller/template_data_pipelines 
cd template_data_pipelines 

# create conda environment with necessary dependencies
conda env create -y -n template_data_pipelines -f environment.yml
conda activate template_data_pipelines

# install project code as local local python module
pip install -e .
```

If using `mamba`, simply replace `conda` with `mamba` in the above commands.

If `git` is not installed on the system, the code can also be downloaded as a zip file from the github website.

## Updating the local code
To update the local code with any changes made to the repo, run
```bash
git pull origin main
pip install -e .
```

Note that will result in an error, if you have modified any files.
To revert any changes, use `git status` to see which files have been modified and then `git reset --hard` to revert the changes rerun the above commands.

# For developers
## Python dependencies
Necessary python packages including versions are declared in the [`environment.yml`](./environment.yml) file
and installed upon creating the `conda` environment.
The packages are typically installed from 
- the `conda-forge` channel
- `pypi` for packages not available on `conda-forge`

## Working with Jupyter notebooks
Jupyter notebooks are a user-friendly way to create and document workflows using a combination of markdown and code cells.
However, they are saved along with lots of metadata in `JSON` format,
which is not well suited for version control.

Here, each notebook is paired with a `.py` script file containing identical code/markdown data.
With this setup, changes to the workflows can be easily tracked in the `.py` files,
while the user can still work with the notebook files.
The conversion is done via the [Jupytext](https://jupytext.readthedocs.io/en/latest/) package, which provides multiple ways to convert between `.ipynb` and `.py` files.

```
└── notebooks
    ├── workflow1.ipynb
    ├── workflow2.ipynb
    └── scripts
        ├── workflow1.py
        └── workflow2.py
```
## Jupytext workflows
Here are a few examples for how to convert between `.ipynb` and `.py` files using Jupytext.

### Manual conversion
The simplest way to convert between `.ipynb` and `.py` files is to use the
[Jupytext CLI](https://jupytext.readthedocs.io/en/latest/using-cli.html).
Note that this process can be further streamlined using the
[Jupytext configuration file](https://jupytext.readthedocs.io/en/latest/config.html)
(see [`pyproject.toml`](./pyproject.toml)).

This repo also provides a command line tool as a wrapper around `jupytext` to convert between all `.ipynb` and `.py` files.
The script is called via
```
# compare timestamps and update older
python src/sync_notebooks.py
```

Note that it is the user's responsibility to ensure that the `.py` and `.ipynb` files are in sync before committing to version control.

### Automatic conversion: pre-commit hooks
Jupytext provides a [pre-commit hook](https://jupytext.readthedocs.io/en/latest/using-pre-commit.html)
that runs `jupytext --sync` everytime you commit notebooks or scripts.
The hook is stored in the [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) file and can be installed running
```
pre-commit install
```

### Automatic conversion: Github Actions
The GitHub Actions workflow that syncs notebooks and script files is stored in 
[`.github/workflows/sync_notebooks.yml.disabled`](./.github/workflows/sync_notebooks.yml.disabled).
To enable it, simply rename the file to `.github/workflows/sync_notebooks.yml` and push the changes to the main branch.
Note that this workflow uses `jupytext` with explicitly defined input and output files instead
of `jupytext --sync`.
Therefore, it ignores the `pyproject.toml` configuration file and
you have to set the `NOTEBOOK_FOLDER` and `SCRIPT_FOLDER` environment variables in the workflow file.

The Actions workflow is triggered on every pull request and pushes to the main branch.
It then syncs notebooks and script files, and adds potiential changes as a new commit to etiher the pull request or directly to the main branch.
Since the Actions bot is creating commits, it is important to enable write permissions for the bot in the repository settings.

Note that this approach compares notebook and script files based on their commit history,
because git does not store file modification times.
If both files have been modified in the same commit,
the Actions workflow will assume that both files are in sync.

### Jupytext extension for VSCode
When working with VSCode, the extension
[Jupytext for Notebooks (congyiwu)](https://marketplace.visualstudio.com/items?itemName=congyiwu.vscode-jupytext)
is recommended.
This allows you to open a `.py` file as a Jupyter notebook.
Changes to that notebook are directly written via Jupytext to the `.py` file
and the `.ipynb` file is never actually stored in the working directory.


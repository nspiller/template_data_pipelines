Template file and folder structure for data pipelines

The file and code structure of this repo is inspired by the 
[The Good Research Code Handbook](https://goodresearch.dev/setup#)
by Patick Mineault.
This handbook is a great resource for setting up a coding projects in academic research.

# Installation
The code in the `src` directory is installed as a local, editable python package.
It is installed via the python package manager `pip` into some `conda` environment
and is then accessible via `from src import ...` in any python script.

## Prerequisites
### Conda 
Download and install [miniforge](https://github.com/conda-forge/miniforge)
(recommended if you do _not_ have Anaconda already installed).
This gives you a light-weight `conda` installation and access to the
faster `mamba` package manager.

If you already do have [Anaconda](https://www.anaconda.com/download) installed,
you can just use this, if you do not want to switch to miniforge.

How to work with `conda` environments can be found in the 
[`mamba`](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#)
or 
[`conda`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
user guides.

### Git
Download and install [`git`](https://git-scm.com/downloads) for your operating system.

While it is not strictly necessary to use `git clone` to download the code,
it is recommended because you can easily get the latest updates via `git pull`
(see below).

## Dependencies
Dependencies on python packages are are stored in the `environment.yml` file.
This file is used to create the `conda` environment needed to run the code in this project.
The packages are typically installed from 
- the `conda-forge` channel
- `pypi` for packages not available on `conda-forge`

## Installing local code
Getting the code up and running on a new system is done via the command in the `conda` prompt (adapt URL and name to your repo):
```
# get source code
git clone https://github.com/nspiller/template_data_pipelines 
cd template_data_pipelines 

# create conda environment with necessary dependencies
conda env create -n template_data_pipelines -f environment.yml
conda activate template_data_pipelines

# install project code as local local python module
pip install -e .

# convert scripts to notebooks
jupytext --sync scripts/*.py
```

If using `mamba`, simply replace `conda` with `mamba` in the above commands.

If `git` is not installed on the system, the code can also be downloaded as a zip file from the github website.

## Updating the local code
```
# update with latest changes
git pull origin main

# convert scripts to notebooks
jupytext --sync scripts/*.py
```

If `git` is not installed on your system, you will have to set up a new environment for the udpated code to avoid any conflicts.

Note that `jupytext --sync` will update the paired `scripts/*py` and `notebooks/*ipynb` based on their time stamp.

# Working with script files
A convenient way to work with python code is via Jupyter notebooks,
which allow for interactive code execution and visualization along with 
documentation in markdown format.
However, 
Jupyter notebooks are saved as `JSON` file, which do not work well with git version control.
Therefore, no Jupyter notebooks, i.e. `.ipynb` files, are stored in this repo.
Instead, they are stored as `.py` python script files in the [`scripts/`](./scripts/) folder.
Note that the `.py` files do not contain any output cells.

These script files can be easily opened as Jupyter notebooks.
This is done via the [`jupytext`](https://jupytext.readthedocs.io/en/latest/index.html)
python module.
This way one has the convenience of working with Jupyter notebooks,
but avoids the problems of version control with `.ipynb` files.

## option 1: Opening script files using the jupytextvscode extension
If you are working with VSCode,
the most convenient way to open the `.py` files as Jupyter notebooks is the extension
[Jupytext for Notebooks (congyiwu)](https://marketplace.visualstudio.com/items?itemName=congyiwu.vscode-jupytext).
This extension adds the option "Open as Jupyter Notebook" to the `.py` files 
(right click on the file in the explorer view).
The `.ipynb` file is never actually stored on disk,
but any changes made to the `.ipynb` file are directly written to the `.py` file.
The `.py` file can then be committed to version control.

## option 2: Manually converting between script and notebook files with the jupytext CLI
`jupytext` can be called from the command line to sync between `.ipynb` and `.py` file.
The [configuration file](./pyproject.toml)
in this repo defines `scripts` as the folder to store `.py` files,
and `notebooks` folder to create the corresponding `.ipynb` files.

Calling `jupytext` on a `.py` file will create the corresponding `.ipynb` file in the `notebooks` folder:
```
jupytext --sync scripts/example.py
[jupytext] Reading scripts/example.py in format py
[jupytext] Updating notebooks/example.ipynb
[jupytext] Updating the timestamp of scripts/example.py
```
Calling `jupytext` again on either the `.py` or the `.ipynb` file will update the contents of the older file with the newer ones.

Note that the `notebooks` folder can be included in the [`.gitignore`](./.gitignore),
so that notebooks to not overcrowd the version control hisotry.
This is adviced if all users of the repo know how to handle the `.py` files.
In this case, it may be useful to create the notebook files in the git releases.

Note that in case you are not using VSCode,
which can run notebooks using only the `ipykernel` module,
you will have to install `conda install jupyter
in your environment to work with Jupyter notebooks.

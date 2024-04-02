import subprocess
from pathlib import Path


def sync(notebook_folder, script_folder):
    """Cycle through Jupyter notebooks and sync with paired Python scripts.

    Parameters
    ----------
    notebook_folder : path-like
        Path to folder where .ipynb files will be saved
    """
    notebook_files = Path(notebook_folder).glob("*.ipynb")
    script_files = Path(script_folder).glob("*.py")
    files = list(notebook_files) + list(script_files)

    for f in files:
        command = f"jupytext --sync {f.as_posix()}"
        print(f">> RUNNING {command}")
        subprocess.run(command.split())

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Convert between Jupyter notebooks and Python scripts using jupytext.",
        epilog="""
        Requires pyproject.toml with jupytext configuration. 
        IMPORTANT: does not handle white spaces in file names
        """,
    )

    args = parser.parse_args()
    sync("notebooks", "notebooks/scripts")
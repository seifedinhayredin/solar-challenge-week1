import nbformat
from nbformat.validator import NotebookValidationError
import sys

notebook_path = sys.argv[1]

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    print(f"{notebook_path} is a valid notebook!")
except NotebookValidationError as e:
    print(f"Notebook validation error: {e}")
except Exception as e:
    print(f"Error reading notebook: {e}")

# Repository Guidelines

## Project Structure & Module Organization

This repository contains standalone Python learning exercises. `week1/W3SchoolsPython/` groups scripts by topic: `variable/`, `datatypes/`, `Strings/`, and `Lists/`. The root `lo_trinh_dsa_ml_dl_3_thang.md` is a study roadmap; `README.md` identifies the project. `project1/` and `week2/` are currently empty. There are no shared Python packages, assets, or test directories yet. Add a new exercise beside related examples, and create a new topic directory only when needed.

## Run and Check Commands

No build step or third-party dependencies are configured. Run a script directly from the repository root, for example:

```bash
python3 week1/W3SchoolsPython/Lists/ListComprehension.py
```

Check a changed script for syntax errors with `python3 -m py_compile path/to/script.py`. This creates a `__pycache__/` directory; remove generated files before committing. Because examples print their results, inspect the output against the lesson's intended behavior.

## Coding Style & Naming Conventions

Use four spaces for indentation in new Python code and keep each exercise self-contained. Prefer descriptive `snake_case` variable and function names for new work. Existing lesson filenames and examples use mixed capitalization; preserve existing names when editing them so references remain valid. Keep explanations close to the example they describe, and use UTF-8 for Vietnamese text. Avoid adding dependencies for simple language demonstrations.

## Testing Guidelines

There is no automated test suite or coverage target. For each changed exercise, run its script and check the printed result and any expected error demonstration. If an exercise grows reusable logic, add focused tests under `tests/` using Python's `unittest`, with files named `test_<topic>.py`; run them with `python3 -m unittest discover -s tests`.

## Commits & Pull Requests

Recent commits use short, informal subject lines such as `List comprehension done`; no formal convention is established. Write a concise subject naming the topic and change, for example `Add list slicing examples`. Keep unrelated lessons in separate commits. In a pull request, describe the exercises changed, the commands run, and the observed output or behavior. Link an issue if one exists; include screenshots only when a visual artifact is involved.

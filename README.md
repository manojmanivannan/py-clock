# Py-Clock

![Pipeline](https://github.com/manojmanivannan/py-clock/actions/workflows/test.yml/badge.svg)
[![latest tag](https://img.shields.io/github/v/tag/manojmanivannan/py-clock.svg?label=latest%20tag&sort=semver)](https://pypi.org/project/py-text-clock/)

A Python CLI tool that prints the current time as a verbose sentence or highlights it in a text matrix.

## Installation

### From PyPI
```bash
pip install py-text-clock
```

## Usage

```bash
Usage: py-clock [OPTIONS]

Options:
  -s, --show    Show the current time
  -m, --matrix  Show time as matrix
  -d, --debug   Run in debug mode
  -h, --help    Show this message and exit.
```

### Examples

**Show current time as a sentence:**
```bash
$ py-clock -s
IT IS TWENTY FIVE MINUTES TO FOUR
```

**Show current time in a matrix:**
```bash
$ py-clock -s -m
```
**I T** L **I S** A S T H T E N<br>
A C F I F T E E N D C O<br>
**T W E N T Y** X **F I V E** W<br>
T H I R T Y F T E N O S<br>
**M I N U T E S** E **T O** U R<br>
P A S T O R U **F O U R** T<br>
S E V E N X T W E L V E<br>
N I N E D I V E C T W O<br>
E I G H T F E L E V E N<br>
S I X T H R E E O N E G<br>
T E N S E Z O' C L O C K


## Local Development Setup

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management.

1. Clone the repository:
   ```bash
   git clone https://github.com/manojmanivannan/py-clock.git
   cd py-clock
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   uv pip install -e .
   # To install testing dependencies:
   uv pip install pytest
   ```

3. Run the CLI tool locally:
   ```bash
   uv run py-clock -s -m
   ```

4. Run the tests:
   ```bash
   uv run pytest
   ```

## Release

1. Update the version in `pyproject.toml`
2. Create and push a new tag:
   ```bash
   git tag <x.x.x>
   git push origin <x.x.x>
   ```

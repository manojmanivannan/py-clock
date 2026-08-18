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
  -a, --analog  Show time as analog clock
  -l, --live    Run continuously as a TUI app (with --matrix or --analog)
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
(Displays the time highlighted within a beautifully styled Rich TUI matrix panel)

**Show current time as an analog clock:**
```bash
$ py-clock -s -a
```
(Displays the time on an analog clock face rendered in the terminal)

**Run continuously (Live Mode):**
```bash
$ py-clock -s -m -l   # Live updating matrix clock
$ py-clock -s -a -l   # Live updating analog clock
```
(Starts a continuously updating TUI clock that refreshes every second)


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

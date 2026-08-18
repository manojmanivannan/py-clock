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

#### Analog
```bash
$ py-clock -s -a -l
╭───────── Analog Clock ──────────╮
│               12                │
│        11             1         │
│                                 │
│   10                       2    │
│             H                   │
│              H        MMM       │
│               H   MMMM          │
│  9             OMM           3  │
│               .                 │
│               .                 │
│              .             4    │
│    8        .                   │
│             .                   │
│         7  .          5         │
│                6                │
╰─────────────────────────────────╯
$
```
#### Matrix
<pre><code>$ py-clock -s -m
╭──────── Py-Clock ────────╮
│ <b>I T</b> L <b>I S</b> A S T H <b>T E N</b>  │
│ A C F I F T E E N D C O  │
│ T W E N T Y X F I V E W  │
│ T H I R T Y F T E N O S  │
│ R <b>M I N U T E S</b> E T O U  │
│ <b>P A S T</b> O R U F O U R T  │
│ S E V E N X T W E L V E  │
│ N I N E F I V E C T W O  │
│ E I G H T F <b>E L E V E N</b>  │
│ S I X T H R E E O N E G  │
│ T E N S E Z O' C L O C K │
╰──────────────────────────╯</code></pre>

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

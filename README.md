# ocean_read_the_docs

A repository to generate documentation from doc strings

## Setup

### Prerequisites

1. Python 3.9.2

### Initial setup

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
git submodule update --init --recursive
git submodule update --recursive --remote
```

### Generate markdowns

```
python generate_markdowns.py -l ocean.py aquarius provider
```

### Script options

- `-l` : List of apps
- `-v` : Verbose logging
- `-m` : List of modules (optional). If not provided, scirpt will generate docs for all the modules.

### Usage:

Generate the markdowns and push the changes to `main` branch. Refresh the [Ocean Procotol docs](https://github.com/oceanprotocol/docs) deployment.

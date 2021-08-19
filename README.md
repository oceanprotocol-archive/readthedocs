# ocean_read_the_docs

A repository to generate documentation from doc strings

## Setup

### Prerequisites

1. Python 3.8+

### Initial setup

```bash
python -m venv venv

source venv/bin/activate
# or, if Python 3.9: source venv/Scripts/activate

pip install wheel
pip install -r requirements.txt
git submodule update --init --recursive

git submodule foreach -q --recursive 'git checkout $(git config -f $toplevel/.gitmodules submodule.$name.branch || echo main)'

git pull "$@" &&
  git submodule sync --recursive &&
  git submodule update --init --recursive
```

### Generate markdowns

```
python generate_markdowns.py -l ocean.py aquarius provider ocean-subgraph
```

### Script options

- `-l` : List of apps
- `-v` : Verbose logging
- `-m` : List of modules (optional). If not provided, scirpt will generate docs for all the modules.

### Usage:

Generate the markdowns and push the changes to `main` branch or raise a PR and merge changes to `main`.

Refresh the [Ocean Procotol docs](https://github.com/oceanprotocol/docs) deployment by creating a new PR with a dummy commit.

1. Clone `docs` repository and create a new branch.
2. `git commit --allow-empty -m "Trigger rebuild"`.
3. Push the changes.
4. Create a new PR.
5. Merge the PR to `main`.

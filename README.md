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

### Usage:

1. Check if intended submodule points to correct branch and has all the required commits. Submodules will be cloned in `submodules` directory. If not, pull the changes from remote submodule.

- Check branch

  `cd submodules/ocean.py && git branch`

- Check commits

  `git log`

  `cd ../..`

2. Checkout new feature branch.
   `git checkout -b feature/<name>`

3. Generate the markdowns.

   `python generate_markdowns.py -l ocean.py aquarius provider ocean-subgraph`

4. Stage, Commit and Push changes

   `git add .`

   `git commit -m "message"`

   `git push origin <branchnam>`

5. Create a pull request and merge changes to `main` branch.

6. Refresh the [Ocean Procotol docs](https://github.com/oceanprotocol/docs) deployment by creating a new PR with a dummy commit.

- Clone `docs` repository and create a new branch.
- `git commit --allow-empty -m "Trigger rebuild"`.
- Push the changes.
- Create a new PR.
- Merge the PR to `main`.

### Script options

- `-l` : List of apps
- `-v` : Verbose logging
- `-m` : List of modules (optional). If not provided, scirpt will generate docs for all the modules.

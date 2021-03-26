# ocean_read_the_docs
A repository to generate documentation from doc strings

## Setup

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
git submodule update --init --recursive
git submodule update --recursive --remote
python generate_markdowns.py
```
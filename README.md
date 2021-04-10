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

### Generate markdown and serve on website
```
python generate_markdowns.py
```
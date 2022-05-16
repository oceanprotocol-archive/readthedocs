---
title: config
slug: aquarius/config
app: aquarius
module: aquarius.config
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.4/aquarius/config.py
version: 3.1.4
---
## Config

```python
class Config(configparser.ConfigParser)
```

#### \_\_init\_\_

```python
 | def __init__(filename=None, **kwargs)
```

Reads the content of `filename` and sets the config values.

#### db\_url

```python
 | @property
 | def db_url()
```

**Returns**:

Database url (hostname:port)


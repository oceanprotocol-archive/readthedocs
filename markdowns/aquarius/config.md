---
title: config
slug: /read-the-docs/aquarius/config
app: aquarius
module: aquarius.config
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


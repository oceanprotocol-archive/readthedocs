---
title: example_config
slug: ocean_lib/example_config
app: ocean.py
module: ocean_lib.example_config
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/example_config.py
version: 0.5.26
---
## ExampleConfig

```python
class ExampleConfig()
```

#### get\_config\_net

```python
 | @staticmethod
 | def get_config_net()
```

**Returns**:

value of environment variable `TEST_NET` or default `ganache`

#### get\_base\_config

```python
 | @staticmethod
 | def get_base_config()
```

**Returns**:

dict

#### get\_network\_config

```python
 | @staticmethod
 | def get_network_config(network_name)
```

**Returns**:

dict

#### get\_config\_dict

```python
 | @staticmethod
 | def get_config_dict(network_name=None)
```

**Returns**:

dict

#### get\_config

```python
 | @staticmethod
 | def get_config(network_name=None)
```

**Returns**:

`Config` instance


---
title: example_config
slug: ocean_lib/example_config
app: ocean.py
module: ocean_lib.example_config
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-bumpversion-to-v0.7.0/ocean_lib/example_config.py
version: 0.7.0
---
## ExampleConfig

```python
class ExampleConfig()
```

#### get\_config

```python
 | @staticmethod
 | @enforce_types
 | def get_config() -> Config
```

Return `Config` containing default values for a given network.
Chain ID is determined by querying the RPC specified by `OCEAN_NETWORK_URL` envvar.


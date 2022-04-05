---
title: example_config
slug: ocean_lib/example_config
app: ocean.py
module: ocean_lib.example_config
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/example_config.py
version: 1.0.0-alpha.2
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


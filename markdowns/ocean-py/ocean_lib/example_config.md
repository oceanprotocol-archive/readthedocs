---
title: example_config
slug: ocean_lib/example_config
app: ocean.py
module: ocean_lib.example_config
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/example_config.py
version: 0.5.30
---
#### NETWORK\_NAME

The interval in seconds between calls for the latest block number.

## ExampleConfig

```python
@enforce_types
class ExampleConfig()
```

#### get\_config

```python
 | @staticmethod
 | def get_config() -> Config
```

Return `Config` containing default values for a given network.
Chain ID is determined by querying the RPC specified by `NETWORK_URL` envvar.


---
title: config
slug: ocean_provider/config
app: provider
module: ocean_provider.config
source: https://github.com/oceanprotocol/provider/blob/v0.4.18-8-g361885d/ocean_provider/config.py
version: 0.4.19
---
Config data.

## Config

```python
class Config(configparser.ConfigParser)
```

Class to manage the squid-py configuration.

#### \_\_init\_\_

```python
 | def __init__(filename=None, options_dict=None, **kwargs)
```

Initialize Config class.

Options available:

[eth-network]
network = http://localhost:8545                            # ocean-contracts url.

[resources]
aquarius.url = http://localhost:5000

**Arguments**:

- `filename`: Path of the config file, str.
- `options_dict`: Python dict with the config, dict.
- `kwargs`: Additional args. If you pass text, you have to pass the plain text
configuration.

#### network\_url

```python
 | @property
 | def network_url()
```

URL of the evm network. (e.g.): http://localnetwork:8545.

#### operator\_service\_url

```python
 | @property
 | def operator_service_url()
```

URL of the operator service component. (e.g.): http://myoperatorservice:8050.

#### storage\_path

```python
 | @property
 | def storage_path()
```

Path to local storage (database file).


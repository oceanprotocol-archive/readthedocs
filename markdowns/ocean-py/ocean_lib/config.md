---
title: config
slug: ocean_lib/config
app: ocean.py
module: ocean_lib.config
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/config.py
---
## Config

```python
class Config(configparser.ConfigParser)
```

Class to manage the ocean-lib configuration.

#### \_\_init\_\_

```python
 | def __init__(filename=None, options_dict=None, **kwargs)
```

Initialize Config class.

Options available:
```
[eth-network]
; ethereum network url
network = rinkeby
; Path of json abis, this defaults to the artifacts installed with `pip install ocean-contracts`
artifacts.path = artifacts

[resources]
metadata_cache_uri = http://localhost:5000
provider.url = http://localhost:8030

[util]
typecheck = true
```

**Arguments**:

- `filename`: Path of the config file, str.
- `options_dict`: Python dict with the config, dict.
- `kwargs`: Additional args. If you pass text, you have to pass the plain text configuration.

#### artifacts\_path

```python
 | @property
 | def artifacts_path()
```

Path where the contracts artifacts are allocated.

#### network\_url

```python
 | @property
 | def network_url()
```

URL of the ethereum network. (e.g.): http://mynetwork:8545.

#### gas\_limit

```python
 | @property
 | def gas_limit()
```

Ethereum gas limit.

#### metadata\_cache\_uri

```python
 | @property
 | def metadata_cache_uri()
```

URL of metadata cache component. (e.g.): http://myaquarius:5000.

#### provider\_address

```python
 | @property
 | def provider_address()
```

Provider address (e.g.): 0x00bd138abd70e2f00903268f3db08f2d25677c9e.

Ethereum address of service provider

#### downloads\_path

```python
 | @property
 | def downloads_path()
```

Path for the downloads of assets.


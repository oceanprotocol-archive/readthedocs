---
title: config
slug: ocean_lib/config
app: ocean.py
module: ocean_lib.config
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-update-docs/ocean_lib/config.py
version: 0.6.1
---
## Config

```python
class Config(configparser.ConfigParser)
```

Class to manage the ocean-lib configuration.

#### \_\_init\_\_

```python
 | def __init__(filename: Optional[Union[Path, str]] = None, options_dict: Optional[Dict[str, Any]] = None, **kwargs, ,) -> None
```

Initialize Config class.

Options available:
```
[eth-network]
; ethereum network url
network = https://rinkeby.infura.io/v3/<your Infura project id>

[resources]
metadata_cache_uri = http://localhost:5000
provider.url = http://localhost:8030
```

**Arguments**:

- `filename`: Path of the config file, str.
- `options_dict`: Python dict with the config, dict.
- `kwargs`: Additional args. If you pass text, you have to pass the plain text configuration.

#### block\_confirmations

```python
 | @property
 | @enforce_types
 | def block_confirmations() -> Integer
```

Block confirmations.

#### network\_url

```python
 | @property
 | @enforce_types
 | def network_url() -> str
```

URL of the ethereum network. (e.g.): http://mynetwork:8545.

#### network\_name

```python
 | @property
 | @enforce_types
 | def network_name() -> str
```

Name of the ethereum network. (e.g.): ganache.

#### chain\_id

```python
 | @property
 | @enforce_types
 | def chain_id() -> int
```

Chain ID of the ethereum network. (e.g.): 1337.

#### gas\_limit

```python
 | @property
 | @enforce_types
 | def gas_limit() -> int
```

Ethereum gas limit.

#### metadata\_cache\_uri

```python
 | @property
 | @enforce_types
 | def metadata_cache_uri() -> str
```

URL of metadata cache component. (e.g.): http://myaquarius:5000.

#### provider\_address

```python
 | @property
 | @enforce_types
 | def provider_address() -> str
```

Provider address (e.g.): 0x00bd138abd70e2f00903268f3db08f2d25677c9e.

Ethereum address of service provider

#### downloads\_path

```python
 | @property
 | @enforce_types
 | def downloads_path() -> str
```

Path for the downloads of assets.


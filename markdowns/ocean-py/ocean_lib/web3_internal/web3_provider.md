---
title: web3_provider
slug: ocean_lib/web3_internal/web3_provider
app: ocean.py
module: ocean_lib.web3_internal.web3_provider
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/web3_internal/web3_provider.py
version: 0.5.22
---
## Web3Provider

```python
class Web3Provider(object)
```

Provides the Web3 instance.

#### init\_web3

```python
 | @staticmethod
 | def init_web3(network_url=None, provider=None)
```

One of `network_url` or `provider` is required.

If `provider` is given, `network_url` will be ignored.

**Arguments**:

- `network_url`: 
- `provider`: 

**Returns**:



#### get\_web3

```python
 | @staticmethod
 | def get_web3(network_url=None, provider=None)
```

Return the web3 instance to interact with the ethereum client.

#### set\_web3

```python
 | @staticmethod
 | def set_web3(web3)
```

Set web3 instance.


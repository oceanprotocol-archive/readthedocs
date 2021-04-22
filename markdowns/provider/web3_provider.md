---
title: web3_provider
slug: /read-the-docs/provider/web3_provider
app: provider
module: web3_internal.web3_provider
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


---
title: web3_provider
slug: /read-the-docs/ocean-py/web3_provider
section: ocean.py
sub_section: web3_internal
---
<a name="web3_internal.web3_provider"></a>
# web3\_internal.web3\_provider

<a name="web3_internal.web3_provider.Web3Provider"></a>
## Web3Provider Objects

```python
class Web3Provider(object)
```

Provides the Web3 instance.

<a name="web3_internal.web3_provider.Web3Provider.init_web3"></a>
#### init\_web3

```python
 | @staticmethod
 | init_web3(network_url=None, provider=None)
```

One of `network_url` or `provider` is required.

If `provider` is given, `network_url` will be ignored.

**Arguments**:

- `network_url`: 
- `provider`: 

**Returns**:



<a name="web3_internal.web3_provider.Web3Provider.get_web3"></a>
#### get\_web3

```python
 | @staticmethod
 | get_web3(network_url=None, provider=None)
```

Return the web3 instance to interact with the ethereum client.


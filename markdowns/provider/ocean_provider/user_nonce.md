---
title: user_nonce
slug: ocean_provider/user_nonce
app: provider
module: ocean_provider.user_nonce
source: https://github.com/oceanprotocol/provider/blob/v0.4.24/ocean_provider/user_nonce.py
version: 0.4.24
---
#### get\_nonce

```python
def get_nonce(address)
```

**Returns**:

`nonce` for the given address stored in the database

#### increment\_nonce

```python
def increment_nonce(address)
```

Increments the value of `nonce` in the database
:param: address


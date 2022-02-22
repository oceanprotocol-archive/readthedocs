---
title: user_nonce
slug: ocean_provider/user_nonce
app: provider
module: ocean_provider.user_nonce
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/user_nonce.py
version: 0.4.17
---
#### get\_nonce

```python
def get_nonce(address)
```

**Returns**:

`nonce` for the given address stored in the database

#### update\_nonce

```python
def update_nonce(address, nonce_value)
```

Updates the value of `nonce` in the database
:param: address
:param: nonce_value


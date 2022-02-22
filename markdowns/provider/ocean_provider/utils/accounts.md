---
title: accounts
slug: ocean_provider/utils/accounts
app: provider
module: ocean_provider.utils.accounts
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/utils/accounts.py
version: 0.4.17
---
#### verify\_signature

```python
def verify_signature(signer_address, signature, original_msg, nonce)
```

**Returns**:

True if signature is valid

#### get\_private\_key

```python
def get_private_key(wallet)
```

Returns private key of the given wallet

#### sign\_message

```python
def sign_message(message, wallet)
```

**Arguments**:

- `message`: str
- `wallet`: Wallet instance

**Returns**:

`hex` value of the signed message


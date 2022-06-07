---
title: accounts
slug: ocean_provider/utils/accounts
app: provider
module: ocean_provider.utils.accounts
source: https://github.com/oceanprotocol/provider/blob/v1.0.16/ocean_provider/utils/accounts.py
version: 1.0.16
---
#### verify\_signature

```python
def verify_signature(signer_address, signature, original_msg, nonce)
```

**Returns**:

True if signature is valid, throws InvalidSignatureError otherwise

#### get\_private\_key

```python
def get_private_key(wallet)
```

Returns the private key of the given wallet.

#### sign\_message

```python
def sign_message(message, wallet)
```

Signs the message with the private key of the given Wallet

**Arguments**:

- `message`: str
- `wallet`: Wallet instance

**Returns**:

signature


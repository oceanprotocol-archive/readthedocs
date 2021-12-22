---
title: encryption
slug: ocean_provider/utils/encryption
app: provider
module: ocean_provider.utils.encryption
source: https://github.com/oceanprotocol/provider/blob/v0.4.18-8-g361885d/ocean_provider/utils/encryption.py
version: 0.4.19
---
#### do\_encrypt

```python
def do_encrypt(document, wallet=None, public_key=None)
```

**Arguments**:

- `document`: Json document/string to be encrypted
- `wallet`: Wallet instance
- `public_key`: Eth public address

**Returns**:

Encrypted String

#### do\_decrypt

```python
def do_decrypt(encrypted_document, provider_wallet)
```

**Arguments**:

- `encrypted_document`: Encrypted data
- `provider_wallet`: Wallet instance

**Returns**:

Decrypted string if successful else `None`


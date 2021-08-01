---
title: encryption
slug: ocean_provider/utils/encryption
app: provider
module: ocean_provider.utils.encryption
source: https://github.com/oceanprotocol/provider/blob/issue-182-improve-docs/ocean_provider/utils/encryption.py
version: 0.4.12
---
#### do\_encrypt

```python
def do_encrypt(document, wallet: Wallet = None, public_key=None)
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


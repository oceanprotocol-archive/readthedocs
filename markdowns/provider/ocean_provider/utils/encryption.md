---
title: encryption
slug: ocean_provider/utils/encryption
app: provider
module: ocean_provider.utils.encryption
source: https://github.com/oceanprotocol/provider/blob/v1.0.16/ocean_provider/utils/encryption.py
version: 1.0.16
---
#### do\_encrypt

```python
def do_encrypt(document: Union[HexStr, str, bytes], wallet: LocalAccount = None, public_key: str = None) -> HexStr
```

**Arguments**:

- `document`: document to be encrypted as HexStr or bytes
- `wallet`: LocalAccount instance
- `public_key`: Eth public address

**Returns**:

Encrypted String

#### do\_decrypt

```python
def do_decrypt(encrypted_document: Union[HexStr, bytes], provider_wallet: LocalAccount) -> bytes
```

**Arguments**:

- `encrypted_document`: Encrypted document as HexStr or bytes
- `provider_wallet`: LocalAccount instance

**Returns**:

Decrypted string


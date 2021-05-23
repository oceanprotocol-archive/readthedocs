---
title: transactions
slug: None
app: ocean.py
module: ocean_lib.web3_internal.transactions
---
#### sign\_hash

```python
@enforce_types_shim
def sign_hash(msg_hash, wallet: Wallet) -> str
```

This method use `personal_sign`for signing a message. This will always prepend the
`\x19Ethereum Signed Message:\n32` prefix before signing.

**Arguments**:

- `msg_hash`: 
- `wallet`: Wallet instance

**Returns**:

signature


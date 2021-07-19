---
title: transactions
slug: ocean_lib/web3_internal/transactions
app: ocean.py
module: ocean_lib.web3_internal.transactions
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/web3_internal/transactions.py
version: 0.5.26
---
#### sign\_hash

```python
@enforce_types
def sign_hash(msg_hash, wallet: Wallet) -> str
```

This method use `personal_sign`for signing a message. This will always prepend the
`\x19Ethereum Signed Message:\n32` prefix before signing.

**Arguments**:

- `msg_hash`: 
- `wallet`: Wallet instance

**Returns**:

signature


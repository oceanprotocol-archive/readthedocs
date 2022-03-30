---
title: wallet
slug: ocean_lib/web3_internal/wallet
app: ocean.py
module: ocean_lib.web3_internal.wallet
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/web3_internal/wallet.py
version: 1.0.0-alpha.1
---
## Wallet

```python
class Wallet()
```

The wallet is responsible for signing transactions and messages by using an account's
private key.

The use of this wallet allows Ocean tools to send rawTransactions which keeps the user
key and password safe and they are never sent outside. Another advantage of this is that
we can interact directly with remote network nodes without having to run a local parity
node since we only send the raw transaction hash so the user info is safe.

Usage:
```python
wallet = Wallet(
    ocean.web3,
    private_key=private_key,
    block_confirmations=ocean.config.block_confirmations,
    transaction_timeout=config.transaction_timeout,
)
```

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(web3: Web3, private_key: str, block_confirmations: Union[Integer, int], transaction_timeout: Union[Integer, int]) -> None
```

Initialises Wallet object.

#### sign

```python
 | @enforce_types
 | def sign(msg_hash: SignableMessage) -> SignedMessage
```

Sign a transaction.


---
title:web3_internal-wallet
slug:/docs/ocean-py/web3_internal-wallet
section:ocean-py
---
<a name="web3_internal.wallet"></a>
# web3\_internal.wallet

<a name="web3_internal.wallet.Wallet"></a>
## Wallet Objects

```python
class Wallet()
```

The wallet is responsible for signing transactions and messages by using an account's
private key.

The private key is always read from the encrypted keyfile and is never saved in memory beyond
the life span of the signing function.

The use of this wallet allows Ocean tools to send rawTransactions which keeps the user
key and password safe and they are never sent outside. Another advantage of this is that
we can interact directly with remote network nodes without having to run a local parity
node since we only send the raw transaction hash so the user info is safe.

<a name="web3_internal.wallet.Wallet.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(web3, private_key: typing.Union[str, None] = None, encrypted_key: dict = None, password: typing.Union[str, None] = None, address: typing.Union[str, None] = None)
```

Initialises Wallet object.


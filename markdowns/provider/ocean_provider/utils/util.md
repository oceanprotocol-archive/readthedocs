---
title: util
slug: ocean_provider/utils/util
app: provider
module: ocean_provider.utils.util
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/utils/util.py
version: 1.0.9
---
#### sign\_tx

```python
def sign_tx(web3, tx, private_key)
```

**Arguments**:

- `web3`: Web3 object instance
- `tx`: transaction
- `private_key`: Private key of the account

**Returns**:

rawTransaction (str)

#### sign\_and\_send

```python
def sign_and_send(web3: Web3, transaction: TxParams, from_account: LocalAccount) -> Tuple[HexStr, TxReceipt]
```

Returns the transaction id and transaction receipt.

#### sign\_send\_and\_wait\_for\_receipt

```python
def sign_send_and_wait_for_receipt(web3: Web3, transaction: TxParams, from_account: LocalAccount) -> Tuple[HexStr, TxReceipt]
```

Returns the transaction id and transaction receipt.


---
title: utils
slug: ocean_lib/web3_internal/web3_overrides/utils
app: ocean.py
module: ocean_lib.web3_internal.web3_overrides.utils
source: https://github.com/oceanprotocol/ocean.py/blob/v0.8.6/ocean_lib/web3_internal/web3_overrides/utils.py
version: 0.8.6
---
#### wait\_for\_transaction\_receipt\_and\_block\_confirmations

```python
@enforce_types
def wait_for_transaction_receipt_and_block_confirmations(web3: Web3, tx_hash: HexBytes, block_confirmations: int, block_number_poll_interval: float, transaction_timeout: int = 120) -> TxReceipt
```

Wait for the transaction receipt. Then, verify the transaction receipt
still appears in the chain after `block_confirmations` number of blocks.
Return the transaction receipt.

**Arguments**:

- `web3`: Web3, used to query for transaction receipts and block number.
- `tx_hash`: HexBytes, the transaction hash.
- `block_confirmations`: int, number of blocks to wait before confirming
transaction is still in chain. Larger number of block confirmations
increases certainty that transaction has settled.
- `block_number_poll_interval`: float, amount of time between calls to
get latest block number in seconds
- `transaction_timeout`: int, amount of time to wait for initial tx
receipt in seconds.


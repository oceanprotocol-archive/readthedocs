---
title: contract
slug: ocean_lib/web3_internal/web3_overrides/contract
app: ocean.py
module: ocean_lib.web3_internal.web3_overrides.contract
source: https://github.com/oceanprotocol/ocean.py/blob/v0.8.5-1-g11c361d/ocean_lib/web3_internal/web3_overrides/contract.py
version: 0.8.5
---
## CustomContractFunction

```python
@enforce_types
class CustomContractFunction()
```

#### \_\_init\_\_

```python
 | def __init__(contract_function)
```

Initializes CustomContractFunction.

#### transact

```python
 | def transact(transaction: Dict[str, Any], block_confirmations: int, transaction_timeout: int) -> HexBytes
```

Customize calling smart contract transaction functions.
This function is copied from web3 ContractFunction with a few changes:

1. Don't set `from` using the web3.eth.default account
2. Add chainId if `chainId` is not in the `transaction` dict
3. Estimate gas limit if `gas` is not in the `transaction` dict

**Arguments**:

- `transaction`: dict which has the required transaction arguments

**Returns**:

hex str transaction hash

#### transact\_with\_contract\_function

```python
@enforce_types
def transact_with_contract_function(address: str, web3: Web3, block_confirmations: int, transaction_timeout: int, function_name: Optional[str] = None, transaction: Optional[dict] = None, contract_abi: Optional[list] = None, fn_abi: Optional[dict] = None, *args, **kwargs, *, ,) -> HexBytes
```

Helper function for interacting with a contract function by sending a
transaction. This is copied from web3 `transact_with_contract_function`
with a few additions:
    1. If `account_key` in transaction dict, sign and send transaction via
       `web3.eth.send_raw_transaction`
    2. Otherwise, send via `web3.eth.send_transaction`
    3. Retry failed transactions (when txn_receipt.status indicates failure)
    4. Network-dependent timeout


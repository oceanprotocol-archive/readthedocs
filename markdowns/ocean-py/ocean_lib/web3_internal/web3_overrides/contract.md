---
title: contract
slug: None
app: ocean.py
module: ocean_lib.web3_internal.web3_overrides.contract
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/web3_internal/web3_overrides/contract.py
---
## CustomContractFunction

```python
class CustomContractFunction()
```

#### \_\_init\_\_

```python
 | def __init__(contract_function)
```

Initializes CustomContractFunction.

#### transact

```python
 | def transact(transaction)
```

Customize calling smart contract transaction functions.

Use `personal_sendTransaction` instead of `eth_sendTransaction` and to estimate gas limit.

This function is largely copied from web3 ContractFunction with an important addition.

Note: will fallback to `eth_sendTransaction` if `passphrase` is not provided in the
`transaction` dict.

**Arguments**:

- `transaction`: dict which has the required transaction arguments per
`personal_sendTransaction` requirements.

**Returns**:

hex str transaction hash

#### transact\_with\_contract\_function

```python
def transact_with_contract_function(address, web3, function_name=None, transaction=None, contract_abi=None, fn_abi=None, *args, **kwargs, *, ,)
```

Helper function for interacting with a contract function by sending a
transaction. This is copied from web3 `transact_with_contract_function`
so we can use `personal_sendTransaction` when possible.


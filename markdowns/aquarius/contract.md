---
title: contract
slug: /read-the-docs/aquarius/contract
section: aquarius
sub_section: web3_internal.web3_overrides
---
<a name="web3_internal.web3_overrides.contract"></a>
# web3\_internal.web3\_overrides.contract

<a name="web3_internal.web3_overrides.contract.CustomContractFunction"></a>
## CustomContractFunction Objects

```python
class CustomContractFunction()
```

<a name="web3_internal.web3_overrides.contract.CustomContractFunction.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(contract_function)
```

Initializes CustomContractFunction.

<a name="web3_internal.web3_overrides.contract.CustomContractFunction.transact"></a>
#### transact

```python
 | transact(transaction)
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

<a name="web3_internal.web3_overrides.contract.transact_with_contract_function"></a>
#### transact\_with\_contract\_function

```python
transact_with_contract_function(address, web3, function_name=None, transaction=None, contract_abi=None, fn_abi=None, *args, **kwargs, *, ,)
```

Helper function for interacting with a contract function by sending a
transaction. This is copied from web3 `transact_with_contract_function`
so we can use `personal_sendTransaction` when possible.


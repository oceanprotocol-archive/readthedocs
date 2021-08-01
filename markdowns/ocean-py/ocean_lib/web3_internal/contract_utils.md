---
title: contract_utils
slug: ocean_lib/web3_internal/contract_utils
app: ocean.py
module: ocean_lib.web3_internal.contract_utils
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/web3_internal/contract_utils.py
version: 0.5.26
---
#### get\_contract\_definition

```python
def get_contract_definition(contract_name)
```

Returns the abi JSON for a contract name.

#### load\_contract

```python
@enforce_types
def load_contract(web3: Web3, contract_name, address)
```

Loads a contract using its name and address.

#### get\_contracts\_addresses

```python
def get_contracts_addresses(network, address_file)
```

Get addresses for all contract names, per network and address_file given.


---
title: contract_utils
slug: ocean_lib/web3_internal/contract_utils
app: ocean.py
module: ocean_lib.web3_internal.contract_utils
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/web3_internal/contract_utils.py
version: 1.0.0-alpha.1
---
#### get\_contract\_definition

```python
@enforce_types
def get_contract_definition(contract_name: str) -> Dict[str, Any]
```

Returns the abi JSON for a contract name.

#### load\_contract

```python
@enforce_types
def load_contract(web3: Web3, contract_name: str, address: Optional[str]) -> Contract
```

Loads a contract using its name and address.

#### get\_contracts\_addresses

```python
@enforce_types
def get_contracts_addresses(network: str, address_file: str) -> Optional[Dict[str, str]]
```

Get addresses for all contract names, per network and address_file given.


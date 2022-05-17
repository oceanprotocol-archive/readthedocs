---
title: address
slug: ocean_provider/utils/address
app: provider
module: ocean_provider.utils.address
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/utils/address.py
version: 1.0.9
---
#### get\_address\_json

```python
def get_address_json(address_path: Union[str, Path]) -> Dict[str, Any]
```

Return the json object of all Ocean contract addresses on all chains.

#### get\_contract\_address

```python
def get_contract_address(address_path: str, contract_name: str, chain_id: int) -> HexAddress
```

Return the contract address with the given name and chain id


---
title: datatoken
slug: ocean_provider/utils/datatoken
app: provider
module: ocean_provider.utils.datatoken
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/utils/datatoken.py
version: 0.4.17
---
#### get\_datatoken\_contract

```python
def get_datatoken_contract(web3: Web3, address: Optional[str] = None) -> Contract
```

Build a web3 Contract instance using the Ocean Protocol ERC20Template ABI.

This function assumes that the `ERC20Template` stored at index 1 of the
`ERC721Factory` provides all the functionality needed by Provider,
especially the `getMetaData` contract method.


---
title: datatoken
slug: ocean_provider/utils/datatoken
app: provider
module: ocean_provider.utils.datatoken
source: https://github.com/oceanprotocol/provider/blob/v1.0.16/ocean_provider/utils/datatoken.py
version: 1.0.16
---
#### get\_datatoken\_contract

```python
def get_datatoken_contract(web3: Web3, address: Optional[str] = None) -> Contract
```

Build a web3 Contract instance using the Ocean Protocol ERC20Template ABI.

This function assumes that the `ERC20Template` stored at index 1 of the
`ERC721Factory` provides all the functionality needed by Provider,
especially the `getMetaData` contract method.

#### verify\_order\_tx

```python
def verify_order_tx(web3: Web3, datatoken_address: HexAddress, tx_id: HexStr, service: Service, amount: int, sender: HexAddress, extra_data: None, allow_expired_provider_fees=False)
```

Check order tx and provider fees validity on-chain for the given parameters.


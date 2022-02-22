---
title: data_nft
slug: ocean_provider/utils/data_nft
app: provider
module: ocean_provider.utils.data_nft
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/utils/data_nft.py
version: 0.4.17
---
#### get\_data\_nft\_contract

```python
def get_data_nft_contract(web3: Web3, address: Optional[str] = None) -> Contract
```

Build a web3 Contract instance using the Ocean Protocol ERC721Template ABI.

This function assumes that the standard `ERC721Template` stored at index 1
of the `ERC721Factory` provides all the functionality needed by Provider,
especially the `getMetaData` contract method.

#### get\_metadata

```python
def get_metadata(web3: Web3, address: str) -> Tuple[str, str, MetadataState, bool]
```

Queries the ERC721 Template smart contract getMetaData call.
Returns metaDataDecryptorUrl, metaDataDecryptorAddress, metaDataState, and hasMetaData


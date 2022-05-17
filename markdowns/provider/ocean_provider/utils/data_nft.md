---
title: data_nft
slug: ocean_provider/utils/data_nft
app: provider
module: ocean_provider.utils.data_nft
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/utils/data_nft.py
version: 1.0.9
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

#### get\_metadata\_logs\_from\_tx\_receipt

```python
def get_metadata_logs_from_tx_receipt(web3: Web3, tx_receipt: TxReceipt, data_nft_address) -> Iterable[EventData]
```

Selects MetadataCreated or MetadataUpdated log based on tx receipt.


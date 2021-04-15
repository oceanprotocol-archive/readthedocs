---
title: asset_downloader
slug: /read-the-docs/ocean-py/asset_downloader
section: ocean.py
sub_section: assets
---
<a name="assets.asset_downloader"></a>
# assets.asset\_downloader

<a name="assets.asset_downloader.download_asset_files"></a>
#### download\_asset\_files

```python
@enforce_types_shim
download_asset_files(service_index: int, asset: Asset, consumer_wallet: Wallet, destination: str, token_address: str, order_tx_id: str, data_provider: Type[DataServiceProvider], index: Optional[int] = None)
```

Download asset data files or result files from a compute job.

**Arguments**:

- `service_index`: identifier of the service inside the asset DDO, str
- `asset`: Asset instance
- `consumer_wallet`: Wallet instance of the consumer
- `destination`: Path, str
- `token_address`: hex str the address of the DataToken smart contract
- `order_tx_id`: hex str the transaction hash of the startOrder tx
- `data_provider`: DataServiceProvider class object
- `index`: Index of the document that is going to be downloaded, int

**Returns**:

Asset folder path, str


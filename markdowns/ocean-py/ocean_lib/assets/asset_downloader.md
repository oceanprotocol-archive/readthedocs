---
title: asset_downloader
slug: ocean_lib/assets/asset_downloader
app: ocean.py
module: ocean_lib.assets.asset_downloader
source: https://github.com/oceanprotocol/ocean.py/blob/v0.8.6/ocean_lib/assets/asset_downloader.py
version: 0.8.6
---
#### download\_asset\_files

```python
@enforce_types
def download_asset_files(service_index: int, asset: V3Asset, consumer_wallet: Wallet, destination: str, token_address: str, order_tx_id: str, data_provider: Type[DataServiceProvider], index: Optional[int] = None, userdata: Optional[dict] = None) -> str
```

Download asset data files or result files from a compute job.

**Arguments**:

- `service_index`: identifier of the service inside the asset DDO, str
- `asset`: V3Asset instance
- `consumer_wallet`: Wallet instance of the consumer
- `destination`: Path, str
- `token_address`: hex str the address of the DataToken smart contract
- `order_tx_id`: hex str the transaction hash of the startOrder tx
- `data_provider`: DataServiceProvider class object
- `index`: Index of the document that is going to be downloaded, int

**Returns**:

asset folder path, str


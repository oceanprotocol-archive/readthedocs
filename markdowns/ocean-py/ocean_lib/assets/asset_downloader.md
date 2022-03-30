---
title: asset_downloader
slug: ocean_lib/assets/asset_downloader
app: ocean.py
module: ocean_lib.assets.asset_downloader
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/assets/asset_downloader.py
version: 1.0.0-alpha.1
---
#### download\_asset\_files

```python
@enforce_types
def download_asset_files(asset: Asset, service: Service, consumer_wallet: Wallet, destination: str, order_tx_id: Union[str, bytes], index: Optional[int] = None, userdata: Optional[dict] = None) -> str
```

Download asset data file or result file from compute job.

**Arguments**:

- `asset`: Asset instance
- `service`: Sevice instance
- `consumer_wallet`: Wallet instance of the consumer
- `destination`: Path, str
- `order_tx_id`: hex str or hex bytes the transaction hash of the startOrder tx
- `index`: Index of the document that is going to be downloaded, Optional[int]
- `userdata`: Dict of additional data from user

**Returns**:

asset folder path, str


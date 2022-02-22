---
title: basics
slug: ocean_provider/utils/basics
app: provider
module: ocean_provider.utils.basics
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/utils/basics.py
version: 0.4.17
---
#### get\_config

```python
def get_config(config_file: Optional[str] = None) -> Config
```

**Returns**:

Config instance

#### get\_provider\_wallet

```python
def get_provider_wallet(web3: Optional[Web3] = None)
```

**Returns**:

Wallet instance

#### get\_web3

```python
def get_web3(network_url: Optional[str] = None) -> Web3
```

**Returns**:

`Web3` instance

#### get\_asset\_from\_metadatastore

```python
def get_asset_from_metadatastore(metadata_url, document_id)
```

**Returns**:

`Ddo` instance


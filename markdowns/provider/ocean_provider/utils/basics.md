---
title: basics
slug: ocean_provider/utils/basics
app: provider
module: ocean_provider.utils.basics
source: https://github.com/oceanprotocol/provider/blob/issue-182-improve-docs/ocean_provider/utils/basics.py
version: 0.4.12
---
#### get\_config

```python
def get_config(config_file: Optional[str] = None) -> Config
```

**Returns**:

Config instance

#### get\_provider\_wallet

```python
def get_provider_wallet(web3: Optional[Web3] = None) -> Wallet
```

**Returns**:

Wallet instance

#### get\_datatoken\_minter

```python
def get_datatoken_minter(datatoken_address)
```

**Returns**:

Eth account address of the Datatoken minter

#### get\_artifacts\_path

```python
def get_artifacts_path()
```

**Returns**:

Path to the artifact directory

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


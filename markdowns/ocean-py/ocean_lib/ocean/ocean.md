---
title: ocean
slug: ocean_lib/ocean/ocean
app: ocean.py
module: ocean_lib.ocean.ocean
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-update-docs/ocean_lib/ocean/ocean.py
version: 0.6.1
---
Ocean module.

## Ocean

```python
class Ocean()
```

The Ocean class is the entry point into Ocean Protocol.

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(config: Union[Dict, Config], data_provider: Optional[Type] = None) -> None
```

Initialize Ocean class.

Usage: Make a new Ocean instance

`ocean = Ocean({...})`

This class provides the main top-level functions in ocean protocol:
1. Publish assets metadata and associated services
- Each asset is assigned a unique DID and a DID Document (DDO)
- The DDO contains the asset's services including the metadata
- The DID is registered on-chain with a URL of the metadata store
to retrieve the DDO from

`asset = ocean.assets.create(metadata, publisher_wallet)`

2. Discover/Search assets via the current configured metadata store (Aquarius)

- Usage:
`assets_list = ocean.assets.search('search text')`

An instance of Ocean is parameterized by a `Config` instance.

**Arguments**:

- `config`: `Config` instance
- `data_provider`: `DataServiceProvider` instance

#### create\_data\_token

```python
 | @enforce_types
 | def create_data_token(name: str, symbol: str, from_wallet: Wallet, cap: int = DataToken.DEFAULT_CAP, blob: str = "") -> DataToken
```

This method deploys a datatoken contract on the blockchain.

Usage:
```python
config = Config('config.ini')
ocean = Ocean(config)
wallet = Wallet(ocean.web3, private_key=private_key, block_confirmations=config.block_confirmations)
datatoken = ocean.create_data_token("Dataset name", "dtsymbol", from_wallet=wallet)
```

**Arguments**:

- `name`: Datatoken name, str
- `symbol`: Datatoken symbol, str
- `from_wallet`: wallet instance, wallet
- `cap`: Amount of data tokens to create, denoted in wei, int

**Returns**:

`Datatoken` instance

#### get\_data\_token

```python
 | @enforce_types
 | def get_data_token(token_address: str) -> DataToken
```

**Arguments**:

- `token_address`: Token contract address, str

**Returns**:

`Datatoken` instance

#### get\_dtfactory

```python
 | @enforce_types
 | def get_dtfactory(dtfactory_address: str = "") -> DTFactory
```

**Arguments**:

- `dtfactory_address`: contract address, str

**Returns**:

`DTFactory` instance

#### get\_user\_orders

```python
 | @enforce_types
 | def get_user_orders(address: str, datatoken: Optional[str] = None, service_id: Optional[int] = None) -> List[Order]
```

**Returns**:

List of orders `[Order]`


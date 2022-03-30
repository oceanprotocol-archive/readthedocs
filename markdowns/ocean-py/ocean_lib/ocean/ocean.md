---
title: ocean
slug: ocean_lib/ocean/ocean
app: ocean.py
module: ocean_lib.ocean.ocean
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/ocean/ocean.py
version: 1.0.0-alpha.1
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

#### create\_erc721\_nft

```python
 | @enforce_types
 | def create_erc721_nft(name: str, symbol: str, from_wallet: Wallet, token_uri: Optional[str] = "https://oceanprotocol.com/nft/", template_index: Optional[int] = 1, additional_erc20_deployer: Optional[str] = None, additional_metadata_updater: Optional[str] = None) -> ERC721NFT
```

This method deploys a ERC721 token contract on the blockchain.
Usage:
```python
config = Config('config.ini')
ocean = Ocean(config)
wallet = Wallet(
ocean.web3,
private_key=private_key,
block_confirmations=config.block_confirmations,
transaction_timeout=config.transaction_timeout,
)
erc721_nft = ocean.create_erc721_nft("Dataset name", "dtsymbol", from_wallet=wallet)
```

**Arguments**:

- `name`: ERC721 token name, str
- `symbol`: ERC721 token symbol, str
- `from_wallet`: wallet instance, wallet
- `template_index`: Template type of the token, int
- `additional_erc20_deployer`: Address of another ERC20 deployer, str
- `token_uri`: URL for ERC721 token, str

**Returns**:

`ERC721NFT` instance

#### get\_nft\_token

```python
 | @enforce_types
 | def get_nft_token(token_address: str) -> ERC721NFT
```

**Arguments**:

- `token_address`: Token contract address, str

**Returns**:

`ERC721NFT` instance

#### get\_datatoken

```python
 | @enforce_types
 | def get_datatoken(token_address: str) -> ERC20Token
```

**Arguments**:

- `token_address`: Token contract address, str

**Returns**:

`ERC20Token` instance

#### get\_nft\_factory

```python
 | @enforce_types
 | def get_nft_factory(nft_factory_address: str = "") -> ERC721FactoryContract
```

**Arguments**:

- `nft_factory_address`: contract address, str

**Returns**:

`ERC721FactoryContract` instance

#### get\_user\_orders

```python
 | @enforce_types
 | def get_user_orders(address: str, datatoken: Optional[str] = None) -> List[AttributeDict]
```

**Returns**:

List of orders `[Order]`


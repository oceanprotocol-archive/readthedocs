---
title: ocean_assets
slug: ocean_lib/ocean/ocean_assets
app: ocean.py
module: ocean_lib.ocean.ocean_assets
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/ocean/ocean_assets.py
version: 1.0.0-alpha.1
---
Ocean module.

## OceanAssets

```python
class OceanAssets()
```

Ocean asset class for V4.

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(config: Config, web3: Web3, data_provider: Type[DataServiceProvider]) -> None
```

Initialises OceanAssets object.

#### validate

```python
 | @enforce_types
 | def validate(asset: Asset) -> Tuple[bool, list]
```

Validate that the asset is ok to be stored in aquarius.

**Arguments**:

- `asset`: Asset.

**Returns**:

(bool, list) list of errors, empty if valid

#### create

```python
 | def create(metadata: dict, publisher_wallet: Wallet, encrypted_files: Optional[str] = None, services: Optional[list] = None, credentials: Optional[dict] = None, provider_uri: Optional[str] = None, erc721_address: Optional[str] = None, erc721_name: Optional[str] = None, erc721_symbol: Optional[str] = None, erc721_template_index: Optional[int] = 1, erc721_additional_erc_deployer: Optional[str] = None, erc721_additional_metadata_updater: Optional[str] = None, erc721_uri: Optional[str] = None, erc20_templates: Optional[List[int]] = None, erc20_names: Optional[List[str]] = None, erc20_symbols: Optional[List[str]] = None, erc20_minters: Optional[List[str]] = None, erc20_fee_managers: Optional[List[str]] = None, erc20_publish_market_order_fee_addresses: Optional[List[str]] = None, erc20_publish_market_order_fee_tokens: Optional[List[str]] = None, erc20_caps: Optional[List[int]] = None, erc20_publish_market_order_fee_amounts: Optional[List[int]] = None, erc20_bytess: Optional[List[List[bytes]]] = None, deployed_erc20_tokens: Optional[List[ERC20Token]] = None, encrypt_flag: Optional[bool] = False, compress_flag: Optional[bool] = False) -> Optional[Asset]
```

Register an asset on-chain.

Creating/deploying a ERC721NFT contract and in the Metadata store (Aquarius).

**Arguments**:

- `metadata`: dict conforming to the Metadata accepted by Ocean Protocol.
- `publisher_wallet`: Wallet of the publisher registering this asset.
- `encrypted_files`: str of the files that need to be encrypted before publishing.
- `services`: list of Service objects.
- `credentials`: credentials dict necessary for the asset.
- `provider_uri`: str URL of service provider. This will be used as base to
construct the serviceEndpoint for the `access` (download) service
- `erc721_address`: hex str the address of the ERC721 token. The new
asset will be associated with this ERC721 token address.
- `erc721_name`: str name of ERC721 token if creating a new one
- `erc721_symbol`: str symbol of ERC721 token  if creating a new one
- `erc721_template_index`: int template index of the ERC721 token, by default is 1.
- `erc721_additional_erc_deployer`: str address of an additional ERC20 deployer.
- `erc721_additional_metadata_updater`: str address of an additional metadata updater.
- `erc721_uri`: str URL of the ERC721 token.
- `erc20_templates`: list of templates indexes for deploying ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_names`: list of names for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_symbols`: list of symbols for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_minters`: list of minters for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_fee_managers`: list of fee managers for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_publish_market_order_fee_addresses`: list of publishing market addresses for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_publish_market_order_fee_tokens`: list of fee tokens for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_caps`: list of cap values for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_publish_market_order_fee_amounts`: list of fee values for ERC20 tokens if deployed_erc20_tokens is None.
- `erc20_bytess`: list of arrays of bytes for deploying ERC20 tokens, default empty (currently not used, useful for future) if deployed_erc20_tokens is None.
- `deployed_erc20_tokens`: list of ERC20 tokens which are already deployed.
- `encrypt_flag`: bool for encryption of the DDO.
- `compress_flag`: bool for compression of the DDO.

**Returns**:

DDO instance

#### update

```python
 | @enforce_types
 | def update(asset: Asset, publisher_wallet: Wallet, provider_uri: Optional[str] = None, encrypt_flag: Optional[bool] = False, compress_flag: Optional[bool] = False) -> Optional[Asset]
```

Update an asset on-chain.

**Arguments**:

- `asset`: The updated asset to update on-chain
- `publisher_wallet`: Wallet of the publisher updating this asset.
- `provider_uri`: str URL of service provider. This will be used as base to construct the serviceEndpoint for the `access` (download) service
- `encrypt_flag`: bool for encryption of the DDO.
- `compress_flag`: bool for compression of the DDO.

**Returns**:

Optional[Asset] the updated Asset or None if updated asset not found in metadata cache

#### search

```python
 | @enforce_types
 | def search(text: str) -> list
```

Search an asset in oceanDB using aquarius.

**Arguments**:

- `text`: String with the value that you are searching

**Returns**:

List of assets that match with the query

#### query

```python
 | @enforce_types
 | def query(query: dict) -> list
```

Search an asset in oceanDB using search query.

**Arguments**:

- `query`: dict with query parameters
(e.g.) https://github.com/oceanprotocol/aquarius/blob/develop/docs/for_api_users/API.md

**Returns**:

List of assets that match with the query.


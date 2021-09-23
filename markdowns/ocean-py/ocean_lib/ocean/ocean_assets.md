---
title: ocean_assets
slug: ocean_lib/ocean/ocean_assets
app: ocean.py
module: ocean_lib.ocean.ocean_assets
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-bumpversion-to-v0.7.0/ocean_lib/ocean/ocean_assets.py
version: 0.7.0
---
Ocean module.

## OceanAssets

```python
class OceanAssets()
```

Ocean assets class.

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(config: Config, web3: Web3, data_provider: Type[DataServiceProvider], ddo_registry_address: str) -> None
```

Initialises OceanAssets object.

#### create

```python
 | @enforce_types
 | def create(metadata: dict, publisher_wallet: Wallet, service_descriptors: list = None, owner_address: Optional[str] = None, data_token_address: Optional[str] = None, provider_uri: Optional[str] = None, dt_name: Optional[str] = None, dt_symbol: Optional[str] = None, dt_blob: Optional[str] = None, dt_cap: Optional[int] = None, encrypt: Optional[bool] = False) -> Optional[Asset]
```

Register an asset on-chain.

Creating/deploying a DataToken contract and in the Metadata store (Aquarius).

**Arguments**:

- `metadata`: dict conforming to the Metadata accepted by Ocean Protocol.
- `publisher_wallet`: Wallet of the publisher registering this asset
- `service_descriptors`: list of ServiceDescriptor tuples of length 2.
The first item must be one of ServiceTypes and the second
item is a dict of parameters and values required by the service
- `owner_address`: hex str the ethereum address to assign asset ownership to. After
registering the asset on-chain, the ownership is transferred to this address
- `data_token_address`: hex str the address of the data token smart contract. The new
asset will be associated with this data token address.
- `provider_uri`: str URL of service provider. This will be used as base to
construct the serviceEndpoint for the `access` (download) service
- `dt_name`: str name of DataToken if creating a new one
- `dt_symbol`: str symbol of DataToken if creating a new one
- `dt_blob`: str blob of DataToken if creating a new one. A `blob` is any text
to be stored with the ERC20 DataToken contract for any purpose.
- `dt_cap`: int amount of DataTokens to mint, denoted in wei

**Returns**:

DDO instance

#### resolve

```python
 | @enforce_types
 | def resolve(did: str) -> Asset
```

When you pass a did retrieve the ddo associated.

**Arguments**:

- `did`: DID, str

**Returns**:

Asset instance

#### search

```python
 | @enforce_types
 | def search(text: str, sort: Optional[dict] = None, offset: Optional[int] = 100, page: Optional[int] = 1, metadata_cache_uri: Optional[str] = None) -> list
```

Search an asset in oceanDB using aquarius.

**Arguments**:

- `text`: String with the value that you are searching
- `sort`: Dictionary to choose order main in some value
- `offset`: Number of elements shows by page
- `page`: Page number
- `metadata_cache_uri`: Url of the aquarius where you want to search. If there is not
provided take the default

**Returns**:

List of assets that match with the query

#### query

```python
 | @enforce_types
 | def query(query: dict, sort: Optional[dict] = None, offset: Optional[int] = 100, page: Optional[int] = 1, metadata_cache_uri: Optional[str] = None) -> list
```

Search an asset in oceanDB using search query.

**Arguments**:

- `query`: dict with query parameters
(e.g.) https://github.com/oceanprotocol/aquarius/blob/develop/docs/for_api_users/API.md
- `sort`: Dictionary to choose order main in some value
- `offset`: Number of elements shows by page
- `page`: Page number
- `metadata_cache_uri`: Url of the aquarius where you want to search. If there is not
provided take the default

**Returns**:

List of assets that match with the query.

#### order

```python
 | @enforce_types
 | def order(did: str, consumer_address: str, service_index: Optional[int] = None, service_type: Optional[str] = None, userdata: Optional[dict] = None) -> OrderRequirements
```

Request a specific service from an asset, returns the service requirements that
must be met prior to consuming the service.

**Arguments**:

- `did`: 
- `consumer_address`: 
- `service_index`: 
- `service_type`: 

**Returns**:

OrderRequirements instance -- named tuple (amount, data_token_address, receiver_address, nonce),

#### pay\_for\_service

```python
 | @staticmethod
 | @enforce_types
 | def pay_for_service(web3: Web3, amount: int, token_address: str, did: str, service_id: int, fee_receiver: str, from_wallet: Wallet, consumer: str) -> str
```

Submits the payment for chosen service in DataTokens.

**Arguments**:

- `amount`: 
- `token_address`: 
- `did`: 
- `service_id`: 
- `fee_receiver`: 
- `from_wallet`: Wallet instance
- `consumer`: str the address of consumer of the service

**Returns**:

hex str id of transfer transaction

#### download

```python
 | @enforce_types
 | def download(did: str, service_index: int, consumer_wallet: Wallet, order_tx_id: str, destination: Union[str, Path], index: Optional[int] = None, userdata: Optional[dict] = None) -> str
```

Consume the asset data.

Using the service endpoint defined in the ddo's service pointed to by service_definition_id.
Consumer's permissions is checked implicitly by the secret-store during decryption
of the contentUrls.
The service endpoint is expected to also verify the consumer's permissions to consume this
asset.
This method downloads and saves the asset datafiles to disk.

**Arguments**:

- `did`: DID, str
- `service_index`: identifier of the service inside the asset DDO, str
- `consumer_wallet`: Wallet instance of the consumer
- `order_tx_id`: hex str id of the token transfer transaction
- `destination`: str path
- `index`: Index of the document that is going to be downloaded, int

**Returns**:

str path to saved files

#### validate

```python
 | @enforce_types
 | def validate(metadata: dict) -> Tuple[bool, list]
```

Validate that the metadata is ok to be stored in aquarius.

**Arguments**:

- `metadata`: dict conforming to the Metadata accepted by Ocean Protocol.

**Returns**:

(bool, list) list of errors, empty if valid

#### owner

```python
 | @enforce_types
 | def owner(did: str) -> str
```

Return the owner of the asset.

**Arguments**:

- `did`: DID, str

**Returns**:

the ethereum address of the owner/publisher of given asset did, hex-str

#### owner\_assets

```python
 | @enforce_types
 | def owner_assets(owner_address: str) -> list
```

List of Asset objects published by ownerAddress

**Arguments**:

- `owner_address`: ethereum address of owner/publisher, hex-str

**Returns**:

list of dids


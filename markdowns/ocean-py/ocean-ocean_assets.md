# Table of Contents

* [ocean.ocean\_assets](#ocean.ocean_assets)
  * [OceanAssets](#ocean.ocean_assets.OceanAssets)
    * [\_\_init\_\_](#ocean.ocean_assets.OceanAssets.__init__)
    * [create](#ocean.ocean_assets.OceanAssets.create)
    * [resolve](#ocean.ocean_assets.OceanAssets.resolve)
    * [search](#ocean.ocean_assets.OceanAssets.search)
    * [query](#ocean.ocean_assets.OceanAssets.query)
    * [order](#ocean.ocean_assets.OceanAssets.order)
    * [pay\_for\_service](#ocean.ocean_assets.OceanAssets.pay_for_service)
    * [download](#ocean.ocean_assets.OceanAssets.download)
    * [validate](#ocean.ocean_assets.OceanAssets.validate)
    * [owner](#ocean.ocean_assets.OceanAssets.owner)
    * [owner\_assets](#ocean.ocean_assets.OceanAssets.owner_assets)

<a name="ocean.ocean_assets"></a>
# ocean.ocean\_assets

Ocean module.

<a name="ocean.ocean_assets.OceanAssets"></a>
## OceanAssets Objects

```python
class OceanAssets()
```

Ocean assets class.

<a name="ocean.ocean_assets.OceanAssets.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(config, data_provider, ddo_registry_address)
```

Initialises OceanAssets object.

<a name="ocean.ocean_assets.OceanAssets.create"></a>
#### create

```python
 | create(metadata: dict, publisher_wallet: Wallet, service_descriptors: list = None, owner_address: str = None, data_token_address: str = None, provider_uri=None, dt_name: str = None, dt_symbol: str = None, dt_blob: str = None, dt_cap: float = None) -> (Asset, None)
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
- `dt_cap`: float

**Returns**:

DDO instance

<a name="ocean.ocean_assets.OceanAssets.resolve"></a>
#### resolve

```python
 | resolve(did: str) -> Asset
```

When you pass a did retrieve the ddo associated.

**Arguments**:

- `did`: DID, str

**Returns**:

Asset instance

<a name="ocean.ocean_assets.OceanAssets.search"></a>
#### search

```python
 | search(text: str, sort=None, offset=100, page=1, aquarius_url=None) -> list
```

Search an asset in oceanDB using aquarius.

**Arguments**:

- `text`: String with the value that you are searching
- `sort`: Dictionary to choose order main in some value
- `offset`: Number of elements shows by page
- `page`: Page number
- `aquarius_url`: Url of the aquarius where you want to search. If there is not
provided take the default

**Returns**:

List of assets that match with the query

<a name="ocean.ocean_assets.OceanAssets.query"></a>
#### query

```python
 | query(query: dict, sort=None, offset=100, page=1, aquarius_url=None) -> []
```

Search an asset in oceanDB using search query.

**Arguments**:

- `query`: dict with query parameters
(e.g.) https://github.com/oceanprotocol/aquarius/blob/develop/docs/for_api_users/API.md
- `sort`: Dictionary to choose order main in some value
- `offset`: Number of elements shows by page
- `page`: Page number
- `aquarius_url`: Url of the aquarius where you want to search. If there is not
provided take the default

**Returns**:

List of assets that match with the query.

<a name="ocean.ocean_assets.OceanAssets.order"></a>
#### order

```python
 | order(did: str, consumer_address: str, service_index: [int, None] = None, service_type: str = None) -> OrderRequirements
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

<a name="ocean.ocean_assets.OceanAssets.pay_for_service"></a>
#### pay\_for\_service

```python
 | @staticmethod
 | pay_for_service(amount: float, token_address: str, did: str, service_id: int, fee_receiver: str, from_wallet: Wallet, consumer: str = None) -> str
```

Submits the payment for chosen service in DataTokens.

**Arguments**:

- `amount`: 
- `token_address`: 
- `did`: 
- `service_id`: 
- `fee_receiver`: 
- `from_wallet`: Wallet instance
- `consumer`: str the address of consumer of the service, defaults to the payer (the `from_wallet` address)

**Returns**:

hex str id of transfer transaction

<a name="ocean.ocean_assets.OceanAssets.download"></a>
#### download

```python
 | download(did: str, service_index: int, consumer_wallet: Wallet, order_tx_id: str, destination: str, index: [int, None] = None) -> str
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

<a name="ocean.ocean_assets.OceanAssets.validate"></a>
#### validate

```python
 | validate(metadata: dict) -> bool
```

Validate that the metadata is ok to be stored in aquarius.

**Arguments**:

- `metadata`: dict conforming to the Metadata accepted by Ocean Protocol.

**Returns**:

bool

<a name="ocean.ocean_assets.OceanAssets.owner"></a>
#### owner

```python
 | owner(did: str) -> str
```

Return the owner of the asset.

**Arguments**:

- `did`: DID, str

**Returns**:

the ethereum address of the owner/publisher of given asset did, hex-str

<a name="ocean.ocean_assets.OceanAssets.owner_assets"></a>
#### owner\_assets

```python
 | owner_assets(owner_address: str) -> list
```

List of Asset objects published by ownerAddress

**Arguments**:

- `owner_address`: ethereum address of owner/publisher, hex-str

**Returns**:

list of dids

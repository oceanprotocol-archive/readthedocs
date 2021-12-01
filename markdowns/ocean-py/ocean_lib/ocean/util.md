---
title: util
slug: ocean_lib/ocean/util
app: ocean.py
module: ocean_lib.ocean.util
source: https://github.com/oceanprotocol/ocean.py/blob/v0.8.5-1-g11c361d/ocean_lib/ocean/util.py
version: 0.8.5
---
#### get\_web3

```python
@enforce_types
def get_web3(network_url: str) -> Web3
```

Return a web3 instance connected via the given network_url.

Adds POA middleware when connecting to the Rinkeby Testnet.

A note about using the `rinkeby` testnet:
Web3 py has an issue when making some requests to `rinkeby`
- the issue is described here: https://github.com/ethereum/web3.py/issues/549
- and the fix is here: https://web3py.readthedocs.io/en/latest/middleware.html#geth-style-proof-of-authority

#### get\_web3\_connection\_provider

```python
@enforce_types
def get_web3_connection_provider(network_url: str) -> Union[CustomHTTPProvider, WebsocketProvider]
```

Return the suitable web3 provider based on the network_url.

Requires going through some gateway such as `infura`.

Using infura has some issues if your code is relying on evm events.
To use events with an infura connection you have to use the websocket interface.

Make sure the `infura` url for websocket connection has the following format
wss://rinkeby.infura.io/ws/v3/357f2fe737db4304bd2f7285c5602d0d
Note the `/ws/` in the middle and the `wss` protocol in the beginning.

**Arguments**:

- `network_url`: str

**Returns**:

provider : Union[CustomHTTPProvider, WebsocketProvider]

#### get\_dtfactory\_address

```python
@enforce_types
def get_dtfactory_address(address_file: str, network: Optional[str] = None, web3: Optional[Web3] = None) -> str
```

Returns the DTFactory address for given network or web3 instance
Requires either network name or web3 instance.

#### get\_bfactory\_address

```python
@enforce_types
def get_bfactory_address(address_file: str, network: Optional[str] = None, web3: Optional[Web3] = None) -> str
```

Returns the BFactory address for given network or web3 instance
Requires either network name or web3 instance.

#### get\_ocean\_token\_address

```python
@enforce_types
def get_ocean_token_address(address_file: str, network: Optional[str] = None, web3: Optional[Web3] = None) -> str
```

Returns the Ocean token address for given network or web3 instance
Requires either network name or web3 instance.


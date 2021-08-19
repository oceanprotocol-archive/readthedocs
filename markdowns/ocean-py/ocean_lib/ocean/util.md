---
title: util
slug: ocean_lib/ocean/util
app: ocean.py
module: ocean_lib.ocean.util
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/ocean/util.py
version: 0.5.30
---
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

A note about using the `rinkeby` testnet:
Web3 py has an issue when making some requests to `rinkeby`
- the issue is described here: https://github.com/ethereum/web3.py/issues/549
- and the fix is here: https://web3py.readthedocs.io/en/latest/middleware.html#geth-style-proof-of-authority

**Arguments**:

- `network_url`: str

**Returns**:

provider : HTTPProvider

#### to\_base

```python
@enforce_types
def to_base(amt: float, dec: int) -> int
```

Returns value in e.g. wei (taking e.g. ETH as input).

#### from\_base

```python
@enforce_types
def from_base(num_base: int, dec: int) -> float
```

Returns value in e.g. ETH (taking e.g. wei as input).

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


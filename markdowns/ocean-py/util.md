---
title: util
slug: /read-the-docs/ocean-py/util
section: ocean.py
sub_section: ocean
---
<a name="ocean.util"></a>
# ocean.util

<a name="ocean.util.get_web3_connection_provider"></a>
#### get\_web3\_connection\_provider

```python
get_web3_connection_provider(network_url)
```

Return the suitable web3 provider based on the network_url.

When connecting to a public ethereum network (mainnet or a test net) without
running a local node requires going through some gateway such as `infura`.

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

<a name="ocean.util.to_base"></a>
#### to\_base

```python
@enforce_types_shim
to_base(amt: float, dec: int) -> int
```

Returns value in e.g. wei (taking e.g. ETH as input).

<a name="ocean.util.from_base"></a>
#### from\_base

```python
@enforce_types_shim
from_base(num_base: int, dec: int) -> float
```

Returns value in e.g. ETH (taking e.g. wei as input).


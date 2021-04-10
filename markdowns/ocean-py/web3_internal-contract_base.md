---
title:web3_internal-contract_base
slug:/docs/ocean-py/web3_internal-contract_base
section:ocean-py
---
<a name="web3_internal.contract_base"></a>
# web3\_internal.contract\_base

All contracts inherit from this base class.

<a name="web3_internal.contract_base.ContractBase"></a>
## ContractBase Objects

```python
class ContractBase(object)
```

Base class for all contract objects.

<a name="web3_internal.contract_base.ContractBase.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(address: [str, None], abi_path=None)
```

Initialises Contract Base object.

The contract name attribute and abi_path are required.

<a name="web3_internal.contract_base.ContractBase.__str__"></a>
#### \_\_str\_\_

```python
 | __str__()
```

Returns contract name @ address.

<a name="web3_internal.contract_base.ContractBase.address"></a>
#### address

```python
 | @property
 | address() -> str
```

Return the ethereum address of the solidity contract deployed in current network.

<a name="web3_internal.contract_base.ContractBase.events"></a>
#### events

```python
 | @property
 | events()
```

Expose the underlying contract's events.

**Returns**:



<a name="web3_internal.contract_base.ContractBase.to_checksum_address"></a>
#### to\_checksum\_address

```python
 | @staticmethod
 | to_checksum_address(address: str)
```

Validate the address provided.

**Arguments**:

- `address`: Address, hex str

**Returns**:

address, hex str

<a name="web3_internal.contract_base.ContractBase.get_tx_receipt"></a>
#### get\_tx\_receipt

```python
 | @staticmethod
 | get_tx_receipt(tx_hash: str, timeout=20)
```

Get the receipt of a tx.

**Arguments**:

- `tx_hash`: hash of the transaction
- `timeout`: int in seconds to wait for transaction receipt

**Returns**:

Tx receipt

<a name="web3_internal.contract_base.ContractBase.get_event_signature"></a>
#### get\_event\_signature

```python
 | get_event_signature(event_name)
```

Return signature of event definition to use in the call to eth_getLogs.

The event signature is used as topic0 (first topic) in the eth_getLogs arguments
The signature reflects the event name and argument types.

**Arguments**:

- `event_name`: 

**Returns**:



<a name="web3_internal.contract_base.ContractBase.subscribe_to_event"></a>
#### subscribe\_to\_event

```python
 | subscribe_to_event(event_name: str, timeout, event_filter, callback=None, timeout_callback=None, args=None, wait=False, from_block="latest", to_block="latest")
```

Create a listener for the event `event_name` on this contract.

**Arguments**:

- `event_name`: name of the event to subscribe, str
- `timeout`: 
- `event_filter`: 
- `callback`: 
- `timeout_callback`: 
- `args`: 
- `wait`: if true block the listener until get the event, bool
- `from_block`: int or None
- `to_block`: int or None

**Returns**:

event if blocking is True and an event is received, otherwise returns None

<a name="web3_internal.contract_base.ContractBase.send_transaction"></a>
#### send\_transaction

```python
 | send_transaction(fn_name: str, fn_args, from_wallet: Wallet, transact: dict = None) -> str
```

Calls a smart contract function.

Uses either `personal_sendTransaction` (if passphrase is available) or `ether_sendTransaction`.

**Arguments**:

- `fn_name`: str the smart contract function name
- `fn_args`: tuple arguments to pass to function above
- `from_wallet`: 
- `transact`: dict arguments for the transaction such as from, gas, etc.

**Returns**:



<a name="web3_internal.contract_base.ContractBase.deploy"></a>
#### deploy

```python
 | @classmethod
 | deploy(cls, web3, deployer_wallet: Wallet, abi_path: str = "", *args)
```

Deploy the DataTokenTemplate and DTFactory contracts to the current network.

**Arguments**:

- `web3`: 
- `abi_path`: 
- `deployer_wallet`: Wallet instance

**Returns**:

smartcontract address of this contract

<a name="web3_internal.contract_base.ContractBase.getLogs"></a>
#### getLogs

```python
 | getLogs(event, web3, argument_filters: Optional[Dict[str, Any]] = None, fromBlock: Optional[BlockIdentifier] = None, toBlock: Optional[BlockIdentifier] = None, blockHash: Optional[HexBytes] = None)
```

Get events for this contract instance using eth_getLogs API.

This is a stateless method, as opposed to createFilter.
It can be safely called against nodes which do not provide
eth_newFilter API, like Infura nodes.
If there are many events,
like ``Transfer`` events for a popular token,
the Ethereum node might be overloaded and timeout
on the underlying JSON-RPC call.
Example - how to get all ERC-20 token transactions
for the latest 10 blocks:
.. code-block:: python
from = max(mycontract.web3.eth.blockNumber - 10, 1)
to = mycontract.web3.eth.blockNumber
events = mycontract.events.Transfer.getLogs(fromBlock=from, toBlock=to)
for e in events:
print(e["args"]["from"],
e["args"]["to"],
e["args"]["value"])
The returned processed log values will look like:
.. code-block:: python
(
AttributeDict({
'args': AttributeDict({}),
'event': 'LogNoArguments',
'logIndex': 0,
'transactionIndex': 0,
'transactionHash': HexBytes('...'),
'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
'blockHash': HexBytes('...'),
'blockNumber': 3
}),
AttributeDict(...),
...
)
See also: :func:`web3.middleware.filter.local_filter_middleware`.

**Arguments**:

- `argument_filters`: 
- `fromBlock`: block number or "latest", defaults to "latest"
- `toBlock`: block number or "latest". Defaults to "latest"
- `blockHash`: block hash. blockHash cannot be set at the
same time as fromBlock or toBlock
:yield: Tuple of :class:`AttributeDict` instances


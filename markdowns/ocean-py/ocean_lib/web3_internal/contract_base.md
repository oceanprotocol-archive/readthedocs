---
title: contract_base
slug: ocean_lib/web3_internal/contract_base
app: ocean.py
module: ocean_lib.web3_internal.contract_base
source: https://github.com/oceanprotocol/ocean.py/blob/HEAD/ocean_lib/web3_internal/contract_base.py
version: 0.5.26
---
All contracts inherit from `ContractBase` class.

## ContractBase

```python
@enforce_types
class ContractBase(object)
```

Base class for all contract objects.

#### \_\_init\_\_

```python
 | def __init__(web3: Web3, address: Optional[str])
```

Initialises Contract Base object.

#### \_\_str\_\_

```python
 | def __str__()
```

Returns contract `name @ address.`

#### configured\_address

```python
 | @classmethod
 | def configured_address(cls, network, address_file)
```

Returns the contract addresses

#### contract\_name

```python
 | @property
 | def contract_name() -> str
```

Returns the contract name

#### address

```python
 | @property
 | def address() -> str
```

Return the ethereum address of the solidity contract deployed in current network.

#### events

```python
 | @property
 | def events()
```

Expose the underlying contract's events.

#### function\_names

```python
 | @property
 | def function_names() -> List[str]
```

Returns the list of functions in the contract

#### to\_checksum\_address

```python
 | @staticmethod
 | def to_checksum_address(address: str)
```

Validate the address provided.

**Arguments**:

- `address`: Address, hex str

**Returns**:

address, hex str

#### get\_tx\_receipt

```python
 | @staticmethod
 | def get_tx_receipt(web3: Web3, tx_hash: str, timeout=20)
```

Get the receipt of a tx.

**Arguments**:

- `tx_hash`: hash of the transaction
- `timeout`: int in seconds to wait for transaction receipt

**Returns**:

Tx receipt

#### is\_tx\_successful

```python
 | def is_tx_successful(tx_hash: str) -> bool
```

Check if the transaction is successful.

**Arguments**:

- `tx_hash`: hash of the transaction

**Returns**:

bool

#### get\_event\_signature

```python
 | def get_event_signature(event_name)
```

Return signature of event definition to use in the call to eth_getLogs.

The event signature is used as topic0 (first topic) in the eth_getLogs arguments
The signature reflects the event name and argument types.

**Arguments**:

- `event_name`: 

**Returns**:



#### subscribe\_to\_event

```python
 | def subscribe_to_event(event_name: str, timeout, event_filter, callback=None, timeout_callback=None, args=None, wait=False, from_block="latest", to_block="latest")
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

#### send\_transaction

```python
 | def send_transaction(fn_name: str, fn_args, from_wallet: Wallet, transact: dict = None) -> str
```

Calls a smart contract function.

Uses either `personal_sendTransaction` (if passphrase is available) or `ether_sendTransaction`.

**Arguments**:

- `fn_name`: str the smart contract function name
- `fn_args`: tuple arguments to pass to function above
- `from_wallet`: 
- `transact`: dict arguments for the transaction such as from, gas, etc.

**Returns**:

hex str transaction hash

#### get\_event\_argument\_names

```python
 | def get_event_argument_names(event_name: str)
```

Finds the event arguments by `event_name`.

**Arguments**:

- `event_name`: str Name of the event to search in the `contract`.

**Returns**:

`event.argument_names` if event is found or None

#### deploy

```python
 | @classmethod
 | def deploy(cls, web3: Web3, deployer_wallet: Wallet, *args)
```

Deploy the DataTokenTemplate and DTFactory contracts to the current network.

**Arguments**:

- `web3`: 
- `deployer_wallet`: Wallet instance

**Returns**:

smartcontract address of this contract

#### get\_event\_log

```python
 | def get_event_log(event_name, from_block, to_block, filters, chunk_size=1000)
```

Retrieves the first event log which matches the filters parameter criteria.
It processes the blocks order backwards.

**Arguments**:

- `event_name`: str
- `from_block`: int
- `to_block`: int
- `filters`: 
- `chunk_size`: int

#### get\_event\_logs

```python
 | def get_event_logs(event_name, from_block, to_block, filters, chunk_size=1000)
```

Fetches the list of event logs between the given block numbers.

**Arguments**:

- `event_name`: str
- `from_block`: int
- `to_block`: int
- `filters`: 
- `chunk_size`: int

**Returns**:

List of event logs. List will have the structure as below.
```Python
[AttributeDict({
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
]
```

#### getLogs

```python
 | @staticmethod
 | def getLogs(event: ContractEvent, argument_filters: Optional[Dict[str, Any]] = None, fromBlock: Optional[BlockIdentifier] = None, toBlock: Optional[BlockIdentifier] = None, blockHash: Optional[HexBytes] = None, from_all_addresses: Optional[bool] = False)
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

```python
from = max(mycontract.web3.eth.block_number - 10, 1)
to = mycontract.web3.eth.block_number
events = mycontract.events.Transfer.getLogs(fromBlock=from, toBlock=to)
for e in events:
print(e["args"]["from"],
e["args"]["to"],
e["args"]["value"])
```
The returned processed log values will look like:

```python
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
```

See also: :func:`web3.middleware.filter.local_filter_middleware`.

**Arguments**:

- `event`: the ContractEvent instance with a web3 instance
- `argument_filters`: 
- `fromBlock`: block number or "latest", defaults to "latest"
- `toBlock`: block number or "latest". Defaults to "latest"
- `blockHash`: block hash. blockHash cannot be set at the
same time as fromBlock or toBlock
- `from_all_addresses`: True = return logs from all addresses
False = return logs originating from event.address
:yield: Tuple of :class:`AttributeDict` instances


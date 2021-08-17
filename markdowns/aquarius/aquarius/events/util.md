---
title: util
slug: aquarius/events/util
app: aquarius
module: aquarius.events.util
source: https://github.com/oceanprotocol/aquarius/blob/main/aquarius/events/util.py
version: 3.0.1
---
#### get\_network\_name

```python
def get_network_name()
```

:return str: network name

#### deploy\_contract

```python
def deploy_contract(w3, _json, private_key, *args)
```

**Arguments**:

- `w3`: Web3 object instance
- `private_key`: Private key of the account
- `_json`: Json content of artifact file
:param *args: arguments to be passed to be constructor of the contract

**Returns**:

address of deployed contract

#### sign\_tx

```python
def sign_tx(web3, tx, private_key)
```

**Arguments**:

- `web3`: Web3 object instance
- `tx`: transaction
- `private_key`: Private key of the account

**Returns**:

rawTransaction (str)

#### deploy\_datatoken

```python
def deploy_datatoken(web3, private_key, name, symbol, minter_address)
```

**Arguments**:

- `web3`: Web3 object instance
- `private_key`: Private key of the account
- `name`: Name of the datatoken to be deployed
- `symbol`: Symbol of the datatoken to be deployed
- `minter_address`: Account address

**Returns**:

Address of the deployed contract

#### get\_address\_file

```python
def get_address_file()
```

Returns Path to the address.json file
Checks envvar first, fallback to address.json included with ocean-contracts.

#### get\_metadata\_contract

```python
def get_metadata_contract(web3)
```

Returns a Contract built from the Metadata contract address (or ENV) and ABI

#### get\_metadata\_start\_block

```python
def get_metadata_start_block()
```

Returns the block number to use as start

#### get\_datatoken\_info

```python
def get_datatoken_info(web3, token_address)
```

**Arguments**:

- `token_address`: Datatoken address

**Returns**:

Json object as below
```
{
"address": <token_address>,
"name": <contract_name>,
"symbol": <symbol>,
"decimals":  <decimals>,
"totalSupply": <totalSupply>,
"cap": <cap>,
"minter": <minter>,
"minterBalance": <balance of minter>,
}
```

#### setup\_web3

```python
def setup_web3(config_file, _logger=None)
```

**Arguments**:

- `config_file`: Web3 object instance
- `_logger`: Logger instance

**Returns**:

web3 instance


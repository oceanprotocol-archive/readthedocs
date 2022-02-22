---
title: util
slug: aquarius/events/util
app: aquarius
module: aquarius.events.util
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.2-62-g1ce2da0/aquarius/events/util.py
version: 3.1.2
---
#### get\_network\_name

```python
def get_network_name()
```

:return str: network name

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
def deploy_datatoken(w3, account, name, symbol)
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

#### get\_metadata\_start\_block

```python
def get_metadata_start_block()
```

Returns the block number to use as start

#### setup\_web3

```python
def setup_web3(config_file, _logger=None)
```

**Arguments**:

- `config_file`: Web3 object instance
- `_logger`: Logger instance

**Returns**:

web3 instance


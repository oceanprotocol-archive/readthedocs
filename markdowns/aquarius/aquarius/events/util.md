---
title: util
slug: aquarius/events/util
app: aquarius
module: aquarius.events.util
source: https://github.com/oceanprotocol/aquarius/blob/issue-517-add-docstrings/aquarius/events/util.py
version: 2.2.12
---
#### get\_network\_name

```python
def get_network_name()
```

:return str: network name

#### prepare\_contracts

```python
def prepare_contracts(web3, config)
```

**Arguments**:

- `web3`: Web3 object instance
- `config`: Config instance

**Returns**:

dict

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

#### get\_artifacts\_path

```python
def get_artifacts_path()
```

**Returns**:

string

#### get\_address\_file

```python
def get_address_file(artifacts_path)
```

**Arguments**:

- `artifacts_path`: Path to the artifacts directory

**Returns**:

string

#### get\_contract\_address\_and\_abi\_file

```python
def get_contract_address_and_abi_file(name)
```

**Arguments**:

- `name`: Artifacts file name

**Returns**:

tuple (contract_address, contract_abi_file)

#### read\_ddo\_contract\_address

```python
def read_ddo_contract_address(file_path, name, network="ganache")
```

**Arguments**:

- `file_path`: Json artifact file path
- `name`: str
- `network`: Name of the network

**Returns**:

tuple (contract_address, contract_abi_file)

#### get\_metadata\_contract

```python
def get_metadata_contract(web3)
```

**Arguments**:

- `web3`: Web3 instance

**Returns**:

Contract instance

#### get\_exchange\_contract

```python
def get_exchange_contract(web3)
```

**Arguments**:

- `web3`: Web3 instance

**Returns**:

Contract instance

#### get\_datatoken\_info

```python
def get_datatoken_info(token_address)
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


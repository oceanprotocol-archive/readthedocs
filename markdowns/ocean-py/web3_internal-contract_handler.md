---
title:web3_internal-contract_handler
slug:/docs/ocean-py/web3_internal-contract_handler
section:ocean-py
---
<a name="web3_internal.contract_handler"></a>
# web3\_internal.contract\_handler

<a name="web3_internal.contract_handler.ContractHandler"></a>
## ContractHandler Objects

```python
class ContractHandler(object)
```

Manages loading contracts and also keeps a cache of loaded contracts.

**Example**:

  contract = ContractHandler.get('DTFactory')
  concise_contract = ContractHandler.get_concise_contract('DTFactory')
  
  It must handle two cases:
  1. One deployment of contract, eg DTFactory
  2. >1 deployments, eg DataTokenTemplate
  
  `Attributes` (_contracts) and methods (e.g. _load) behave accordingly.
  
  `The` _contracts dict maps:
  # 1. (contract_name)                   : (contract, concise_contract)
  # 2. (contract_name, contract_address) : (contract, concise_contract)

<a name="web3_internal.contract_handler.ContractHandler.get"></a>
#### get

```python
 | @staticmethod
 | get(name, address=None)
```

Return the Contract instance for a given name.

**Arguments**:

- `name`: Contract name, str
- `address`: hex str -- address of smart contract

**Returns**:

Contract instance

<a name="web3_internal.contract_handler.ContractHandler.get_concise_contract"></a>
#### get\_concise\_contract

```python
 | @staticmethod
 | get_concise_contract(name, address=None)
```

Return the Concise Contract instance for a given name.

**Arguments**:

- `name`: str -- Contract name
- `address`: hex str -- address of smart contract

**Returns**:

Concise Contract instance

<a name="web3_internal.contract_handler.ContractHandler.set"></a>
#### set

```python
 | @staticmethod
 | set(name, contract)
```

Set a Contract instance for a contract name.

**Arguments**:

- `name`: Contract name, str
- `contract`: Contract instance

<a name="web3_internal.contract_handler.ContractHandler.has"></a>
#### has

```python
 | @staticmethod
 | has(name, address=None)
```

Check if a contract is the ContractHandler contracts.

**Arguments**:

- `name`: Contract name, str
- `address`: hex str -- address of smart contract

**Returns**:

True if the contract is there, bool


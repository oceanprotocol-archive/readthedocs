---
title: contract_handler
slug: /read-the-docs/aquarius/contract_handler
app: aquarius
module: web3_internal.contract_handler
---
## ContractHandler

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

#### get

```python
 | @staticmethod
 | def get(name, address=None)
```

Return the Contract instance for a given name.

**Arguments**:

- `name`: Contract name, str
- `address`: hex str -- address of smart contract

**Returns**:

Contract instance

#### get\_concise\_contract

```python
 | @staticmethod
 | def get_concise_contract(name, address=None)
```

Return the Concise Contract instance for a given name.

**Arguments**:

- `name`: str -- Contract name
- `address`: hex str -- address of smart contract

**Returns**:

Concise Contract instance

#### set

```python
 | @staticmethod
 | def set(name, contract)
```

Set a Contract instance for a contract name.

**Arguments**:

- `name`: Contract name, str
- `contract`: Contract instance

#### has

```python
 | @staticmethod
 | def has(name, address=None)
```

Check if a contract is the ContractHandler contracts.

**Arguments**:

- `name`: Contract name, str
- `address`: hex str -- address of smart contract

**Returns**:

True if the contract is there, bool


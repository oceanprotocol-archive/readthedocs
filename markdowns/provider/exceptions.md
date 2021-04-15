---
title: exceptions
slug: /read-the-docs/provider/exceptions
section: provider
sub_section: web3_internal
---
## OceanKeeperContractsNotFound

```python
class OceanKeeperContractsNotFound(Exception)
```

Raised when is not possible to find the keeper contracts abi.

## OceanDIDNotFound

```python
class OceanDIDNotFound(Exception)
```

Raised when a requested DID or a DID in the chain cannot be found.

## OceanInvalidTransaction

```python
class OceanInvalidTransaction(Exception)
```

Raised when an on-chain transaction fail.


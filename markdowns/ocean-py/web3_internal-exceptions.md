# Table of Contents

* [web3\_internal.exceptions](#web3_internal.exceptions)
  * [OceanKeeperContractsNotFound](#web3_internal.exceptions.OceanKeeperContractsNotFound)
  * [OceanDIDNotFound](#web3_internal.exceptions.OceanDIDNotFound)
  * [OceanInvalidTransaction](#web3_internal.exceptions.OceanInvalidTransaction)

<a name="web3_internal.exceptions"></a>
# web3\_internal.exceptions

<a name="web3_internal.exceptions.OceanKeeperContractsNotFound"></a>
## OceanKeeperContractsNotFound Objects

```python
class OceanKeeperContractsNotFound(Exception)
```

Raised when is not possible to find the keeper contracts abi.

<a name="web3_internal.exceptions.OceanDIDNotFound"></a>
## OceanDIDNotFound Objects

```python
class OceanDIDNotFound(Exception)
```

Raised when a requested DID or a DID in the chain cannot be found.

<a name="web3_internal.exceptions.OceanInvalidTransaction"></a>
## OceanInvalidTransaction Objects

```python
class OceanInvalidTransaction(Exception)
```

Raised when an on-chain transaction fail.

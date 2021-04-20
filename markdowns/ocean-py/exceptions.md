---
title: exceptions
slug: /read-the-docs/ocean-py/exceptions
section: ocean.py
sub_section: ocean_lib
module: ocean_lib.exceptions
---
## OceanEncryptAssetUrlsError

```python
class OceanEncryptAssetUrlsError(Exception)
```

Error invoking the encrypt endpoint.

## InsufficientBalance

```python
class InsufficientBalance(Exception)
```

The token balance is insufficient.

## ContractNotFound

```python
class ContractNotFound(Exception)
```

Contract address is not found in the factory events.

## AquariusError

```python
class AquariusError(Exception)
```

Error invoking an Aquarius metadata service endpoint.

## VerifyTxFailed

```python
class VerifyTxFailed(Exception)
```

Transaction verification failed.


---
title: exceptions
slug: ocean_lib/exceptions
app: ocean.py
module: ocean_lib.exceptions
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/exceptions.py
version: 1.0.0-alpha.2
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

## TransactionFailed

```python
class TransactionFailed(Exception)
```

Transaction has failed.

## DataProviderException

```python
class DataProviderException(Exception)
```

Exception from Provider endpoints.


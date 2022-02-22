---
title: asset
slug: ocean_provider/utils/asset
app: provider
module: ocean_provider.utils.asset
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/utils/asset.py
version: 0.4.17
---
## Asset

```python
class Asset()
```

#### get\_service\_by\_index

```python
 | def get_service_by_index(index: int) -> Service
```

Return the first Service with the given index

#### get\_service\_by\_id

```python
 | def get_service_by_id(service_id: str) -> Service
```

Return the Service with the matching id

#### requires\_address\_credential

```python
 | @property
 | def requires_address_credential() -> bool
```

Checks if an address credential is required on this asset.

#### allowed\_addresses

```python
 | @property
 | def allowed_addresses() -> list
```

Lists addresses that are explicitly allowed in credentials.

#### denied\_addresses

```python
 | @property
 | def denied_addresses() -> list
```

Lists addresesses that are explicitly denied in credentials.

#### is\_consumable

```python
 | def is_consumable(credential: Optional[dict] = None, with_connectivity_check: bool = True, provider_uri: Optional[str] = None) -> ConsumableCodes
```

Checks whether an asset is consumable and returns a ConsumableCode.


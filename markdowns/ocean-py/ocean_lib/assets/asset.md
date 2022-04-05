---
title: asset
slug: ocean_lib/assets/asset
app: ocean.py
module: ocean_lib.assets.asset
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/assets/asset.py
version: 1.0.0-alpha.2
---
## Asset

```python
class Asset(AddressCredential)
```

Asset class to create, import, export, validate Asset/DDO objects for V4.

#### requires\_address\_credential

```python
 | @property
 | @enforce_types
 | def requires_address_credential() -> bool
```

Checks if an address credential is required on this asset.

#### allowed\_addresses

```python
 | @property
 | @enforce_types
 | def allowed_addresses() -> list
```

Lists addresses that are explicitly allowed in credentials.

#### denied\_addresses

```python
 | @property
 | @enforce_types
 | def denied_addresses() -> list
```

Lists addresses that are explicitly denied in credentials.

#### add\_address\_to\_allow\_list

```python
 | @enforce_types
 | def add_address_to_allow_list(address: str) -> None
```

Adds an address to allowed addresses list.

#### add\_address\_to\_deny\_list

```python
 | @enforce_types
 | def add_address_to_deny_list(address: str) -> None
```

Adds an address to the denied addresses list.

#### remove\_address\_from\_allow\_list

```python
 | @enforce_types
 | def remove_address_from_allow_list(address: str) -> None
```

Removes address from allow list (if it exists).

#### remove\_address\_from\_deny\_list

```python
 | @enforce_types
 | def remove_address_from_deny_list(address: str) -> None
```

Removes address from deny list (if it exists).

#### from\_dict

```python
 | @classmethod
 | @enforce_types
 | def from_dict(cls, dictionary: dict) -> "Asset"
```

Import a JSON dict into this Asset.

#### as\_dictionary

```python
 | @enforce_types
 | def as_dictionary() -> dict
```

Return the DDO as a JSON dict.

**Returns**:

dict

#### add\_service

```python
 | @enforce_types
 | def add_service(service: Service) -> None
```

Add a service to the list of services on the V4 DDO.

**Arguments**:

- `service`: To add service, Service

#### get\_service\_by\_id

```python
 | @enforce_types
 | def get_service_by_id(service_id: str) -> Service
```

Return Service with the given id.
Return None if service with the given id not found.

#### get\_service\_by\_index

```python
 | @enforce_types
 | def get_service_by_index(service_index: int) -> Service
```

Return Service with the given index.
Return None if service with the given index not found.

#### get\_index\_of\_service

```python
 | @enforce_types
 | def get_index_of_service(service: Service) -> int
```

Return index of the given Service.
Return None if service was not found.

#### generate\_trusted\_algorithms

```python
 | @enforce_types
 | def generate_trusted_algorithms() -> dict
```

Returns a trustedAlgorithm dictionary for service at index 0.


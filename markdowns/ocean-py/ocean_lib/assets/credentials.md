---
title: credentials
slug: ocean_lib/assets/credentials
app: ocean.py
module: ocean_lib.assets.credentials
source: https://github.com/oceanprotocol/ocean.py/blob/v0.8.5-1-g11c361d/ocean_lib/assets/credentials.py
version: 0.8.5
---
## AddressCredential

```python
class AddressCredential()
```

#### get\_addresses\_of\_class

```python
 | @enforce_types
 | def get_addresses_of_class(access_class: str = "allow") -> list
```

Get a filtered list of addresses from credentials (use with allow/deny).

#### requires\_credential

```python
 | @enforce_types
 | def requires_credential() -> bool
```

Checks whether the asset requires an address credential.

#### validate\_access

```python
 | @enforce_types
 | def validate_access(credential: Optional[dict] = None) -> int
```

Checks a credential dictionary against the address allow/deny lists.

#### add\_address\_to\_access\_class

```python
 | @enforce_types
 | def add_address_to_access_class(address: str, access_class: str = "allow") -> None
```

Adds an address to an address list (either allow or deny).

#### remove\_address\_from\_access\_class

```python
 | @enforce_types
 | def remove_address_from_access_class(address: str, access_class: str = "allow") -> None
```

Removes an address from an address list (either allow or deny)i.

#### get\_address\_entry\_of\_class

```python
 | @enforce_types
 | def get_address_entry_of_class(access_class: str = "allow") -> Optional[dict]
```

Get address credentials entry of the specified access class. access_class = "allow" or "deny".

#### simplify\_credential\_to\_address

```python
@enforce_types
def simplify_credential_to_address(credential: Optional[dict]) -> Optional[str]
```

Extracts address value from credential dictionary.


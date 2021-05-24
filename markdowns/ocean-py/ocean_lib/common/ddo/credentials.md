---
title: credentials
slug: ocean_lib/common/ddo/credentials
app: ocean.py
module: ocean_lib.common.ddo.credentials
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/common/ddo/credentials.py
---
## AddressCredential

```python
class AddressCredential()
```

#### get\_addresses\_of\_class

```python
 | def get_addresses_of_class(access_class="allow")
```

Get a filtered list of addresses from credentials (use with allow/deny).

#### requires\_credential

```python
 | def requires_credential()
```

Checks whether the asset requires an address credential.

#### validate\_access

```python
 | def validate_access(credential=None)
```

Checks a credential dictionary against the address allow/deny lists.

#### add\_address\_to\_access\_class

```python
 | def add_address_to_access_class(address, access_class="allow")
```

Adds an address to an address list (either allow or deny).

#### remove\_address\_from\_access\_class

```python
 | def remove_address_from_access_class(address, access_class="allow")
```

Removes an address from an address list (either allow or deny)i.

#### get\_address\_entry\_of\_class

```python
 | def get_address_entry_of_class(access_class="allow")
```

Get address credentials entry of the specified access class. access_class = "allow" or "deny".

#### get\_lc\_addresses\_from\_entry

```python
 | def get_lc_addresses_from_entry(address_entry)
```

Get an address entry of a given access class from credentials (use with allow/deny).

#### simplify\_credential\_to\_address

```python
def simplify_credential_to_address(credential)
```

Extracts address value from credential dictionary.


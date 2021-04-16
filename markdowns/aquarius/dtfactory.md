---
title: dtfactory
slug: /read-the-docs/aquarius/dtfactory
section: aquarius
sub_section: models
module: models.dtfactory
---
## DTFactory

```python
@enforce_types_shim
class DTFactory(ContractBase)
```

#### verify\_data\_token

```python
 | def verify_data_token(dt_address)
```

Checks that a token was registered.

#### get\_token\_registered\_event

```python
 | def get_token_registered_event(from_block, to_block, token_address)
```

Retrieves event log of token registration.

#### get\_token\_minter

```python
 | def get_token_minter(token_address)
```

Retrieves token minter.

This function will be deprecated in the next major release.
It's only kept for backwards compatibility.

#### get\_token\_address

```python
 | def get_token_address(transaction_id: str) -> str
```

Gets token address using transaction id.


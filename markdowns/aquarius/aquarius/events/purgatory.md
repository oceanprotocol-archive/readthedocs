---
title: purgatory
slug: aquarius/events/purgatory
app: aquarius
module: aquarius.events.purgatory
source: https://github.com/oceanprotocol/aquarius/blob/main/aquarius/events/purgatory.py
version: 3.0.1
---
## Purgatory

```python
class Purgatory()
```

#### retrieve\_new\_list

```python
 | def retrieve_new_list(env_var)
```

**Arguments**:

- `env_var`: Url of the file containing purgatory list.

**Returns**:

Object as follows: {...('<did>', '<reason>'),...}

#### update\_asset\_purgatory\_status

```python
 | def update_asset_purgatory_status(asset, purgatory="true")
```

Updates the field `isInPurgatory` of `asset` object.

#### get\_assets\_authored\_by

```python
 | def get_assets_authored_by(account_address)
```

**Returns**:

List of assets authored by `account_address`

#### update\_lists

```python
 | def update_lists()
```

**Returns**:

None

#### is\_account\_banned

```python
 | def is_account_banned(ref_account_id)
```

**Returns**:

True if `ref_account_id` is in the Purgatory list.


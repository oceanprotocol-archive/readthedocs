---
title: aquarius_provider
slug: ocean_lib/common/aquarius/aquarius_provider
app: ocean.py
module: ocean_lib.common.aquarius.aquarius_provider
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/common/aquarius/aquarius_provider.py
version: 0.8.1
---
## AquariusProvider

```python
@enforce_types
class AquariusProvider()
```

Provides the Aquarius instance.

#### get\_aquarius

```python
 | @staticmethod
 | def get_aquarius(url: str) -> Any
```

Get an Aquarius instance.

#### set\_aquarius\_class

```python
 | @staticmethod
 | def set_aquarius_class(aquarius_class: Any) -> None
```

Set an Aquarius class

**Arguments**:

- `aquarius_class`: Aquarius or similar compatible class


---
title: constants
slug: aquarius/events/constants
app: aquarius
module: aquarius.events.constants
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.2-62-g1ce2da0/aquarius/events/constants.py
version: 3.1.2
---
## SimpleEnum

```python
class SimpleEnum()
```

This class can be used as a replacement for enum.Enum class.
- The attributes are accessible with `ClassName.ATTR`
- :func:`get_value` returns the value for a given key
- :func:`get_all_keys` returns a list of all the keys
- :func:`get_all_values` returns a list of all the values


---
title: event_filter
slug: ocean_lib/web3_internal/event_filter
app: ocean.py
module: ocean_lib.web3_internal.event_filter
source: https://github.com/oceanprotocol/ocean.py/blob/v0.8.6/ocean_lib/web3_internal/event_filter.py
version: 0.8.6
---
## EventFilter

```python
class EventFilter()
```

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(event: ContractEvent, argument_filters: dict = None, from_block: Optional[Union[int, str]] = None, to_block: Optional[Union[int, str]] = None, address: Optional[str] = None, topics: Any = None) -> None
```

Initialises EventFilter.


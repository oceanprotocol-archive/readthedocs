---
title: event_listener
slug: ocean_lib/web3_internal/event_listener
app: ocean.py
module: ocean_lib.web3_internal.event_listener
source: https://github.com/oceanprotocol/ocean.py/blob/issue497-bumpversion-to-v0.7.0/ocean_lib/web3_internal/event_listener.py
version: 0.7.0
---
## EventListener

```python
class EventListener(object)
```

Class representing an event listener.

#### \_\_init\_\_

```python
 | @enforce_types
 | def __init__(web3: Web3, contract_name: str, address: str, event_name: str, args: Optional[list] = None, from_block: Optional[Union[int, str]] = None, to_block: Optional[Union[int, str]] = None, filters: Optional[dict] = None) -> None
```

Initialises EventListener object.

#### make\_event\_filter

```python
 | @enforce_types
 | def make_event_filter() -> EventFilter
```

Create a new event filter.

#### listen\_once

```python
 | @enforce_types
 | def listen_once(callback: Optional[Callable] = None, timeout: Optional[int] = None, timeout_callback: Optional[Callable] = None, start_time: Optional[float] = None, blocking: Optional[bool] = False) -> None
```

Listens once for event.

**Arguments**:

- `callback`: a callback function that takes one argument the event dict
- `timeout`: float timeout in seconds
- `timeout_callback`: a callback function when timeout expires
- `start_time`: float start time in seconds, defaults to current time and is used
for calculating timeout
- `blocking`: bool blocks this call until the event is detected

**Returns**:

event if blocking is True and an event is received, otherwise returns None

#### watch\_one\_event

```python
 | @staticmethod
 | @enforce_types
 | def watch_one_event(event_filter: EventFilter, callback: Callable, timeout_callback: Optional[Callable], timeout: int, args: list, start_time: Optional[int] = None) -> None
```

Start to watch one event.

**Arguments**:

- `event_filter`: 
- `callback`: 
- `timeout_callback`: 
- `timeout`: 
- `args`: 
- `start_time`: 

**Returns**:




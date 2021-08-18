---
title: event_listener
slug: ocean_lib/web3_internal/event_listener
app: ocean.py
module: ocean_lib.web3_internal.event_listener
source: https://github.com/oceanprotocol/ocean.py/blob/HEAD/ocean_lib/web3_internal/event_listener.py
version: 0.5.26
---
## EventListener

```python
class EventListener(object)
```

Class representing an event listener.

#### \_\_init\_\_

```python
 | def __init__(web3, contract_name, address, event_name, args=None, from_block=None, to_block=None, filters=None)
```

Initialises EventListener object.

#### make\_event\_filter

```python
 | def make_event_filter()
```

Create a new event filter.

#### listen\_once

```python
 | def listen_once(callback, timeout=None, timeout_callback=None, start_time=None, blocking=False)
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
 | def watch_one_event(event_filter, callback, timeout_callback, timeout, args, start_time=None)
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




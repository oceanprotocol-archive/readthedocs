---
title: event_listener
slug: /read-the-docs/ocean-py/event_listener
section: ocean.py
sub_section: web3_internal
---
<a name="web3_internal.event_listener"></a>
# web3\_internal.event\_listener

<a name="web3_internal.event_listener.EventListener"></a>
## EventListener Objects

```python
class EventListener(object)
```

Class representing an event listener.

<a name="web3_internal.event_listener.EventListener.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(contract_name, event_name, args=None, from_block=None, to_block=None, filters=None)
```

Initialises EventListener object.

<a name="web3_internal.event_listener.EventListener.make_event_filter"></a>
#### make\_event\_filter

```python
 | make_event_filter()
```

Create a new event filter.

<a name="web3_internal.event_listener.EventListener.listen_once"></a>
#### listen\_once

```python
 | listen_once(callback, timeout=None, timeout_callback=None, start_time=None, blocking=False)
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

<a name="web3_internal.event_listener.EventListener.watch_one_event"></a>
#### watch\_one\_event

```python
 | @staticmethod
 | watch_one_event(event_filter, callback, timeout_callback, timeout, args, start_time=None)
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




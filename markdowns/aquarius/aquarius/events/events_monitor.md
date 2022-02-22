---
title: events_monitor
slug: aquarius/events/events_monitor
app: aquarius
module: aquarius.events.events_monitor
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.2-62-g1ce2da0/aquarius/events/events_monitor.py
version: 3.1.2
---
## EventsMonitor

```python
class EventsMonitor(BlockProcessingClass)
```

Detect on-chain published Metadata and cache it in the database for
fast retrieval and searchability.

The published metadata is extracted from the `MetadataCreated`
event log from the `Metadata` smartcontract. Metadata updates are also detected using
the `MetadataUpdated` event.

The Metadata json object is expected to be
in an `lzma` compressed form and then encrypted. Decryption is done through Provider.

The events monitor pauses for 25 seconds between updates.

The cached Metadata can be restricted to only those published by specific ethereum accounts.
To do this set the `ALLOWED_PUBLISHERS` envvar to the list of ethereum addresses of known publishers.

#### process\_current\_blocks

```python
 | def process_current_blocks()
```

Process all blocks from the last processed block to the current block.

#### process\_block\_range

```python
 | def process_block_range(from_block, to_block)
```

Process a range of blocks.

#### handle\_regular\_event\_processor

```python
 | def handle_regular_event_processor(event_name, processor, processor_args, from_block, to_block)
```

Process emitted events between two given blocks for a given event name.

**Arguments**:

- `event_name` _str_ - event uppercase constant name
- `processor` _EventProcessor_ - event processor
- `processor_args` _List[any]_ - list of processors arguments
- `from_block` _int_ - inital block
- `to_block` _int_ - final block


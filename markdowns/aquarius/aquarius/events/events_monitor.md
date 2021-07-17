---
title: events_monitor
slug: aquarius/events/events_monitor
app: aquarius
module: aquarius.events.events_monitor
source: https://github.com/oceanprotocol/aquarius/blob/main/aquarius/events/events_monitor.py
version: 2.2.12
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
in an `lzma` compressed form. If desired the metadata can also be encrypted for specific
use cases. When using encrypted Metadata, the EventsMonitor requires the private key of
the ethereum account that is used for encryption. This can be specified in `EVENTS_ECIES_PRIVATE_KEY`
envvar.

The events monitor pauses for 25 seconds between updates.

The cached Metadata can be restricted to only those published by specific ethereum accounts.
To do this set the `ALLOWED_PUBLISHERS` envvar to the list of ethereum addresses of known publishers.

#### process_current_blocks

```python
 | def process_current_blocks()
```

Process all blocks from the last processed block to the current block.

#### process_block_range

```python
 | def process_block_range(from_block, to_block)
```

Process a range of blocks.

---
title: processors
slug: aquarius/events/processors
app: aquarius
module: aquarius.events.processors
source: https://github.com/oceanprotocol/aquarius/blob/main/aquarius/events/processors.py
version: 3.0.1
---
## EventProcessor

```python
class EventProcessor(ABC)
```

#### \_\_init\_\_

```python
 | def __init__(event, oceandb, web3, ecies_account, allowed_publishers, purgatory, chain_id)
```

Initialises common Event processing properties.


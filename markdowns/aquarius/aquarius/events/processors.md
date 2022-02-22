---
title: processors
slug: aquarius/events/processors
app: aquarius
module: aquarius.events.processors
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.2-62-g1ce2da0/aquarius/events/processors.py
version: 3.1.2
---
## EventProcessor

```python
class EventProcessor(ABC)
```

#### \_\_init\_\_

```python
 | def __init__(event, dt_contract, sender_address, es_instance, web3, allowed_publishers, purgatory, chain_id)
```

Initialises common Event processing properties.

#### add\_aqua\_data

```python
 | def add_aqua_data(record)
```

Adds keys that are specific to Aquarius, on top of the DDO structure:
event, nft, datatokens.

#### soft\_delete\_ddo

```python
 | def soft_delete_ddo(did: str)
```

Deletes all fields from ES for a given DDO except for the fields listed in AquariusCustomDDOFields

#### update\_aqua\_nft\_state\_data

```python
 | def update_aqua_nft_state_data(new_state: str, did: str)
```

Updates NFT state field from the aquarius custom fields data listed in AquariusCustomDDOFields for a given
DID


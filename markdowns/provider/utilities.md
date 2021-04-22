---
title: utilities
slug: /read-the-docs/provider/utilities
app: provider
module: common.utils.utilities
---
Utilities class

#### generate\_new\_id

```python
def generate_new_id()
```

Generate a new id without prefix.

**Returns**:

Id, str

#### generate\_prefixed\_id

```python
def generate_prefixed_id()
```

Generate a new id prefixed with 0x that is used as identifier for the service agreements ids.

**Returns**:

Id, str

#### to\_32byte\_hex

```python
def to_32byte_hex(web3, val)
```

**Arguments**:

- `web3`: 
- `val`: 

**Returns**:



#### convert\_to\_bytes

```python
def convert_to_bytes(web3, data)
```

**Arguments**:

- `web3`: 
- `data`: 

**Returns**:



#### convert\_to\_string

```python
def convert_to_string(web3, data)
```

**Arguments**:

- `web3`: 
- `data`: 

**Returns**:



#### convert\_to\_text

```python
def convert_to_text(web3, data)
```

**Arguments**:

- `web3`: 
- `data`: 

**Returns**:



#### checksum

```python
def checksum(seed)
```

Calculate the hash3_256.

#### get\_timestamp

```python
def get_timestamp()
```

Return the current system timestamp.


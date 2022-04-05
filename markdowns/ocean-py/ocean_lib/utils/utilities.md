---
title: utilities
slug: ocean_lib/utils/utilities
app: ocean.py
module: ocean_lib.utils.utilities
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.2-1-g9fb6083/ocean_lib/utils/utilities.py
version: 1.0.0-alpha.2
---
Utilities class

#### to\_lpad\_32byte

```python
@enforce_types
def to_lpad_32byte(val: Primitives) -> bytes
```

ecrecover in Solidity expects v as a native uint8, but r and s as left-padded bytes32
This convenience method will add the padding

Adapted from https://web3py.readthedocs.io/en/stable/web3.eth.account.html#prepare-message-for-ecrecover-in-solidity

#### to\_lpad\_32byte\_hex

```python
@enforce_types
def to_lpad_32byte_hex(val: Primitives) -> HexStr
```

ecrecover in Solidity expects v as a native uint8, but r and s as left-padded bytes32
Remix / web3.js expect r and s to be encoded to hex
This convenience method will add the padding and encode to hex

Copied from https://web3py.readthedocs.io/en/stable/web3.eth.account.html#prepare-message-for-ecrecover-in-solidity

#### prepare\_message\_for\_ecrecover\_in\_solidity

```python
@enforce_types
def prepare_message_for_ecrecover_in_solidity(signed_message: SignedMessage) -> Tuple[HexStr, int, str, str]
```

Copied from https://web3py.readthedocs.io/en/stable/web3.eth.account.html#prepare-message-for-ecrecover-in-solidity

#### convert\_to\_bytes

```python
@enforce_types
def convert_to_bytes(data: str) -> bytes
```

**Arguments**:

- `data`: 

**Returns**:



#### convert\_to\_string

```python
@enforce_types
def convert_to_string(data: bytes) -> HexStr
```

**Arguments**:

- `data`: 

**Returns**:



#### convert\_to\_text

```python
@enforce_types
def convert_to_text(data: bytes) -> str
```

**Arguments**:

- `data`: 

**Returns**:



#### create\_checksum

```python
@enforce_types
def create_checksum(text: str) -> str
```

**Returns**:

str


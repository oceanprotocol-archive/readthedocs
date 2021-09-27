---
title: btoken
slug: ocean_lib/models/btoken
app: ocean.py
module: ocean_lib.models.btoken
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/models/btoken.py
version: 0.8.1
---
## BToken

```python
class BToken(ContractBase)
```

#### symbol

```python
 | @enforce_types
 | def symbol() -> str
```

**Returns**:

str

#### decimals

```python
 | @enforce_types
 | def decimals() -> int
```

**Returns**:

int

#### balanceOf

```python
 | @enforce_types
 | def balanceOf(address: str) -> int
```

**Returns**:

int

#### approve

```python
 | @enforce_types
 | def approve(spender_address: str, amt: int, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### transfer

```python
 | @enforce_types
 | def transfer(dst_address: str, amt: int, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### allowance

```python
 | @enforce_types
 | def allowance(src_address: str, dst_address: str) -> int
```

**Returns**:

int


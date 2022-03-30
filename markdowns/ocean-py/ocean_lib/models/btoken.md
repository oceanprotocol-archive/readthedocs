---
title: btoken
slug: ocean_lib/models/btoken
app: ocean.py
module: ocean_lib.models.btoken
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/models/btoken.py
version: 1.0.0-alpha.1
---
## BTokenBase

```python
class BTokenBase(ContractBase)
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

#### increase\_approval

```python
 | @enforce_types
 | def increase_approval(dst: str, amt: int, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### decrease\_approval

```python
 | @enforce_types
 | def decrease_approval(dst: str, amt: int, from_wallet: Wallet)
```

**Returns**:

hex str transaction hash

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

#### transfer\_from

```python
 | @enforce_types
 | def transfer_from(src: str, dst: str, amt: int, from_wallet: Wallet) -> str
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


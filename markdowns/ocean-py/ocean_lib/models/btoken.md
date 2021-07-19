---
title: btoken
slug: ocean_lib/models/btoken
app: ocean.py
module: ocean_lib.models.btoken
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/models/btoken.py
version: 0.5.26
---
## BToken

```python
@enforce_types
class BToken(ContractBase)
```

#### symbol

```python
 | def symbol() -> str
```

:return str:

#### decimals

```python
 | def decimals() -> int
```

:return int:

#### balanceOf

```python
 | def balanceOf(address: str) -> int
```

:return int:

#### approve

```python
 | def approve(spender_address: str, amt_base: int, from_wallet: Wallet)
```

:return str: hex str transaction hash

#### transfer

```python
 | def transfer(dst_address: str, amt_base: int, from_wallet: Wallet)
```

:return str: hex str transaction hash

#### allowance

```python
 | def allowance(src_address: str, dst_address: str) -> int
```

:return int:


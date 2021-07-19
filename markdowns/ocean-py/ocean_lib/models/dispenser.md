---
title: dispenser
slug: ocean_lib/models/dispenser
app: ocean.py
module: ocean_lib.models.dispenser
source: https://github.com/oceanprotocol/ocean.py/blob/issue-384-improve-docs/ocean_lib/models/dispenser.py
version: 0.5.26
---
## DispenserContract

```python
@enforce_types
class DispenserContract(ContractBase)
```

#### is\_active

```python
 | def is_active(dt_address: str) -> bool
```

**Returns**:

bool

#### owner

```python
 | def owner(dt_address: str) -> str
```

**Returns**:

str

#### is\_minter\_approved

```python
 | def is_minter_approved(dt_address: str) -> bool
```

**Returns**:

bool

#### is\_true\_minter

```python
 | def is_true_minter(dt_address: str) -> bool
```

**Returns**:

bool

#### max\_tokens

```python
 | def max_tokens(dt_address: str) -> int
```

**Returns**:

int

#### max\_balance

```python
 | def max_balance(dt_address: str) -> int
```

**Returns**:

int

#### balance

```python
 | def balance(dt_address: str) -> int
```

**Returns**:

int

#### activate

```python
 | def activate(dt_address: str, max_tokens: int, max_balance: int, from_wallet: Wallet)
```

**Returns**:

hex str transaction hash

#### deactivate

```python
 | def deactivate(dt_address: str, from_wallet: Wallet)
```

**Returns**:

hex str transaction hash

#### make\_minter

```python
 | def make_minter(dt_address: str, from_wallet: Wallet)
```

**Returns**:

hex str transaction hash

#### cancel\_minter

```python
 | def cancel_minter(dt_address: str, from_wallet: Wallet)
```

**Returns**:

hex str transaction hash

#### dispense

```python
 | def dispense(dt_address: str, amount: int, from_wallet: Wallet)
```

**Returns**:

hex str transaction hash

#### owner\_withdraw

```python
 | def owner_withdraw(dt_address: str, from_wallet: Wallet)
```

**Returns**:

hex str transaction hash

#### is\_dispensable

```python
 | def is_dispensable(dt_address: str, amount: int, to_wallet: Wallet)
```

**Returns**:

bool


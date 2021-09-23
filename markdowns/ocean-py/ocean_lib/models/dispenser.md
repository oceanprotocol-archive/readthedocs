---
title: dispenser
slug: ocean_lib/models/dispenser
app: ocean.py
module: ocean_lib.models.dispenser
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/models/dispenser.py
version: 0.7.0
---
## DispenserContract

```python
class DispenserContract(ContractBase)
```

#### is\_active

```python
 | @enforce_types
 | def is_active(dt_address: str) -> bool
```

**Returns**:

bool

#### owner

```python
 | @enforce_types
 | def owner(dt_address: str) -> str
```

**Returns**:

str

#### is\_minter\_approved

```python
 | @enforce_types
 | def is_minter_approved(dt_address: str) -> bool
```

**Returns**:

bool

#### is\_true\_minter

```python
 | @enforce_types
 | def is_true_minter(dt_address: str) -> bool
```

**Returns**:

bool

#### max\_tokens

```python
 | @enforce_types
 | def max_tokens(dt_address: str) -> int
```

**Returns**:

int

#### max\_balance

```python
 | @enforce_types
 | def max_balance(dt_address: str) -> int
```

**Returns**:

int

#### balance

```python
 | @enforce_types
 | def balance(dt_address: str) -> int
```

**Returns**:

int

#### activate

```python
 | @enforce_types
 | def activate(dt_address: str, max_tokens: int, max_balance: int, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### deactivate

```python
 | @enforce_types
 | def deactivate(dt_address: str, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### make\_minter

```python
 | @enforce_types
 | def make_minter(dt_address: str, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### cancel\_minter

```python
 | @enforce_types
 | def cancel_minter(dt_address: str, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### dispense

```python
 | @enforce_types
 | def dispense(dt_address: str, amount: int, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### owner\_withdraw

```python
 | @enforce_types
 | def owner_withdraw(dt_address: str, from_wallet: Wallet) -> str
```

**Returns**:

hex str transaction hash

#### is\_dispensable

```python
 | @enforce_types
 | def is_dispensable(dt_address: str, amount: int, to_wallet: Wallet) -> bool
```

**Returns**:

bool


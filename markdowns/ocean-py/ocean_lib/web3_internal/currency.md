---
title: currency
slug: ocean_lib/web3_internal/currency
app: ocean.py
module: ocean_lib.web3_internal.currency
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/web3_internal/currency.py
version: 1.0.0-alpha.1
---
#### ETHEREUM\_DECIMAL\_CONTEXT

ERC20 tokens usually opt for a decimals value of 18, imitating the
relationship between Ether and Wei.

#### DECIMALS\_18

The minimum possible token amount on Ethereum-compatible blockchains, denoted in wei

#### MIN\_WEI

The maximum possible token amount on Ethereum-compatible blockchains, denoted in wei

#### MAX\_WEI

The minimum possible token amount on Ethereum-compatible blockchains, denoted in ether

#### MIN\_ETHER

The maximum possible token amount on Ethereum-compatible blockchains, denoted in ether

#### from\_wei

```python
@enforce_types
def from_wei(amount_in_wei: int, decimals: int = DECIMALS_18) -> Decimal
```

Convert token amount from wei to ether, quantized to the specified number of decimal places.

#### to\_wei

```python
@enforce_types
def to_wei(amount_in_ether: Union[Decimal, str, int], decimals: int = DECIMALS_18) -> int
```

Convert token amount to wei from ether, quantized to the specified number of decimal places
float input is purposfully not supported

#### pretty\_ether\_and\_wei

```python
@enforce_types
def pretty_ether_and_wei(amount_in_wei: int, ticker: str = "") -> str
```

Returns a formatted token amount denoted in wei and human-readable ether
with optional ticker symbol.

This utility is intended for use in log statements, error messages, and
assertions where it is desirable to have both full-precision wei values and
human-readable ether values.

**Examples**:

  pretty_ether_and_wei(123456789_123456789) == "0.123 (123456789123456789 wei)"
  pretty_ether_and_wei(123456789_123456789_12345, "OCEAN") == "12.3K OCEAN (12345678912345678912345 wei)"
  pretty_ether_and_wei(123456789_123456789_123456789, "") == "123M (123456789123456789123456789 wei)"

#### pretty\_ether

```python
@enforce_types
def pretty_ether(amount_in_ether: Union[Decimal, str, int], ticker: str = "", trim: bool = True) -> str
```

Returns a human-readable token amount denoted in ether with optional ticker symbol
Set trim=False to include trailing zeros.

This function assumes the given ether amount is already quantized to
the appropriate number of decimals (like ERC-20 decimals())

**Examples**:

  pretty_ether("0", ticker="OCEAN") == "0 OCEAN"
  pretty_ether("0.01234") == "1.23e-2"
  pretty_ether("1234") == "1.23K"
  pretty_ether("12345678") == "12.3M"
  pretty_ether("1000000.000", trim=False) == "1.00M"
  pretty_ether("123456789012") == "123B"
  pretty_ether("1234567890123") == "1.23e+12"

#### ether\_fmt

```python
@enforce_types
def ether_fmt(amount_in_ether: Union[Decimal, str, int], decimals: int = DECIMALS_18, ticker: str = "") -> str
```

Convert ether amount to a formatted string.

#### moneyfmt

```python
@enforce_types
def moneyfmt(value, places=2, curr="", sep=",", dp=".", pos="", neg="-", trailneg="")
```

Convert Decimal to a money formatted string.
Copied without alteration from https://docs.python.org/3/library/decimal.html#recipes

places:  required number of places after the decimal point
curr:    optional currency symbol before the sign (may be blank)
sep:     optional grouping separator (comma, period, space, or blank)
dp:      decimal point indicator (comma or period)
         only specify as blank when places is zero
pos:     optional sign for positive numbers: '+', space or blank
neg:     optional sign for negative numbers: '-', '(', space or blank
trailneg:optional trailing minus indicator:  '-', ')', space or blank

>>> d = Decimal('-1234567.8901')
>>> moneyfmt(d, curr='$')
'-$1,234,567.89'
>>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
'1.234.568-'
>>> moneyfmt(d, curr='$', neg='(', trailneg=')')
'($1,234,567.89)'
>>> moneyfmt(Decimal(123456789), sep=' ')
'123 456 789.00'
>>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
'<0.02>'

#### normalize\_and\_validate\_ether

```python
@enforce_types
def normalize_and_validate_ether(amount_in_ether: Union[Decimal, str, int]) -> Decimal
```

Returns an amount in ether, encoded as a Decimal
Takes Decimal, str, or int as input. Purposefully does not support float.

#### remove\_trailing\_zeros

```python
@enforce_types
def remove_trailing_zeros(value: Decimal) -> Decimal
```

Returns a Decimal with trailing zeros removed.
Adapted from https://docs.python.org/3/library/decimal.html#decimal-faq


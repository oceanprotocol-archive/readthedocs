---
title: currency
slug: ocean_provider/utils/currency
app: provider
module: ocean_provider.utils.currency
source: https://github.com/oceanprotocol/provider/blob/v0.4.17-69-g5a60369/ocean_provider/utils/currency.py
version: 0.4.17
---
#### MAX\_UINT256

decimal.Context tuned to accomadate MAX_WEI.
* precision=78 because there are 78 digits in MAX_WEI (MAX_UINT256).
  Any lower and decimal operations like quantize throw an InvalidOperation error.
* rounding=ROUND_DOWN (towards 0, aka. truncate) to avoid issue where user
  removes 100% from a pool and transaction fails because it rounds up.

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

#### to\_wei

```python
def to_wei(amount_in_ether: Union[Decimal, str, int], decimals: int = DECIMALS_18) -> int
```

Convert token amount to wei from ether, quantized to the specified number of decimal places
float input is purposfully not supported

#### normalize\_and\_validate\_ether

```python
def normalize_and_validate_ether(amount_in_ether: Union[Decimal, str, int]) -> Decimal
```

Returns an amount in ether, encoded as a Decimal
Takes Decimal, str, or int as input. Purposefully does not support float.


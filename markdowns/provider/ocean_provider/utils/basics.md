---
title: basics
slug: ocean_provider/utils/basics
app: provider
module: ocean_provider.utils.basics
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/utils/basics.py
version: 1.0.9
---
#### get\_config

```python
def get_config(config_file: Optional[str] = None) -> Config
```

**Returns**:

Config instance

#### get\_provider\_wallet

```python
def get_provider_wallet(web3: Optional[Web3] = None)
```

**Returns**:

Wallet instance

#### get\_web3

```python
def get_web3(network_url: Optional[str] = None) -> Web3
```

**Returns**:

`Web3` instance

#### send\_ether

```python
def send_ether(web3, from_wallet: Account, to_address: str, amount: int)
```

Sends ether from wallet to the address.

#### validate\_timestamp

```python
def validate_timestamp(value)
```

Checks whether a timestamp is valid (correctly formed and in the future).


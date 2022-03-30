---
title: erc721_factory
slug: ocean_lib/models/erc721_factory
app: ocean.py
module: ocean_lib.models.erc721_factory
source: https://github.com/oceanprotocol/ocean.py/blob/v1.0.0-alpha.1/ocean_lib/models/erc721_factory.py
version: 1.0.0-alpha.1
---
## ERC721FactoryContract

```python
class ERC721FactoryContract(ERCTokenFactoryBase)
```

#### verify\_nft

```python
 | @enforce_types
 | def verify_nft(nft: str) -> bool
```

Checks that a token was registered.

#### start\_multiple\_token\_order

```python
 | @enforce_types
 | def start_multiple_token_order(orders: List[OrderData], from_wallet: Wallet) -> str
```

An order contains the following keys:

- tokenAddress, str
- consumer, str
- serviceIndex, int
- providerFeeAddress, str
- providerFeeToken, str
- providerFeeAmount (in Wei), int
- providerData, bytes
- v, int
- r, bytes
- s, bytes

#### get\_token\_created\_event

```python
 | @enforce_types
 | def get_token_created_event(from_block: int, to_block: int, token_address: str) -> [AttributeDict]
```

Retrieves event log of token registration.


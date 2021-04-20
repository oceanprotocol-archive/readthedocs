---
title: introduction
slug: /read-the-docs/coean.py/introduction
section: ocean.py
sub_section: introduction
module: 
---
# ocean.py

## What is ocean.py?

ocean.py is part of the [Ocean Protocol](https://www.oceanprotocol.com) toolset. `ocean.py` is a python library that helps to search, publish, and consume datasets in the `Ocean Protocol` ecosystem.

With ocean.py, you can:

- **Publish** data services: downloadable files or compute-to-data.
  Ocean creates a new [ERC20](https://github.com/ethereum/EIPs/blob/7f4f0377730f5fc266824084188cc17cf246932e/EIPS/eip-20.md)
  datatoken for each dataset / data service.
- **Mint** datatokens for the service
- **Sell** datatokens via an OCEAN-datatoken Balancer pool (for auto price discovery), or for a fixed price
- **Stake** OCEAN on datatoken pools
- **Consume** datatokens, to access the service
- **Transfer** datatokens to another owner, and **all other ERC20 actions**
  using [web3.py](https://web3py.readthedocs.io/en/stable/examples.html#working-with-an-erc20-token-contract) etc.

## Installation

`pip install ocean-lib`

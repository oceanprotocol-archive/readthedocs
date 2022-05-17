---
title: chains
slug: aquarius/app/chains
app: aquarius
module: aquarius.app.chains
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.4/aquarius/app/chains.py
version: 3.1.4
---
#### get\_chains\_list

```python
@chains.route("/list", methods=["GET"])
def get_chains_list()
```

Get chains list
---
tags:
  - chains
responses:
  200:
    description: successful operation.
  404:
    description: No chains are present

#### get\_index\_status

```python
@chains.route("/status/<chain_id>", methods=["GET"])
def get_index_status(chain_id)
```

Get index status for a specific chain_id
---
tags:
  - chains
parameters:
  - name: chain_id
    in: path
    description: chainId
    required: true
    type: number
responses:
  200:
    description: successful operation.
  404:
    description: This chainId is not indexed.


---
title: global-statistics.md
slug: examples/python/global-statistics.md
app: ocean-subgraph
module: examples.python.global-statistics
source: https://github.com/oceanprotocol/ocean-subgraph/blob/v1.2.0-3-g56a4192/examples/python/global-statistics.md
version: 1.2.0
---

## Ocean-subgraph python example

Query global statistics like `totalValueLocked`, `totalOceanLiquidity`, `orderCount`, etc.

```python
import requests
import json

base_url = "https://subgraph.rinkeby.oceanprotocol.com"
route = "/subgraphs/name/oceanprotocol/ocean-subgraph"
url = base_url + route

query = """
{
globals {
  id
  totalValueLocked
  totalOceanLiquidity
  totalSwapVolume
  totalOrderVolume
  orderCount
  poolCount
}
}"""

headers = {"Content-Type": "application/json"}

payload = json.dumps({"query": query})
response = requests.request("POST", url, headers=headers, data=payload)
result = json.loads(response.text)

print(result)
```

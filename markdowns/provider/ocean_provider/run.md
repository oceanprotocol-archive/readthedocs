---
title: run
slug: ocean_provider/run
app: provider
module: ocean_provider.run
source: https://github.com/oceanprotocol/provider/blob/v0.4.24/ocean_provider/run.py
version: 0.4.24
---
#### get\_provider\_address

```python
def get_provider_address()
```

Gets the provider wallet address.

#### version

```python
@app.route("/")
def version()
```

Contains the provider data for an user:
    - software;
    - version;
    - network url;
    - provider address;
    - service endpoints, which has all
    the existing endpoints from routes.py.


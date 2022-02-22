---
title: run
slug: aquarius/run
app: aquarius
module: aquarius.run
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.2-62-g1ce2da0/aquarius/run.py
version: 3.1.2
---
This module is the entrypoint for statring the Aquarius component.

#### version

```python
@app.route("/")
def version()
```

**Returns**:

  json object as follows:
  ```JSON
  {
  "plugin":"elasticsearch",
  "software":"Aquarius",
  "version":"2.2.12"
  }
  ```

#### health

```python
@app.route("/health")
def health()
```

Returns conntection db status with mongodb or elasticsearch.

#### spec

```python
@app.route("/spec")
def spec()
```

Returns the information about supported endpoints generated through swagger. Also returns version info, database connection status.


---
title: dao
slug: None
app: aquarius
module: app.dao
source: https://github.com/oceanprotocol/aquarius/blob/main/app/dao.py
---
## Dao

```python
class Dao(object)
```

#### run\_es\_query

```python
 | def run_es_query(data)
```

do an elasticsearch native query.

The query is expected to be in the elasticsearch search format.

**Returns**:

list of objects that match the query.


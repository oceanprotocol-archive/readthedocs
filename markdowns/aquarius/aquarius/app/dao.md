---
title: dao
slug: aquarius/app/dao
app: aquarius
module: aquarius.app.dao
source: https://github.com/oceanprotocol/aquarius/blob/issue-517-add-docstrings/aquarius/app/dao.py
version: 2.2.12
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


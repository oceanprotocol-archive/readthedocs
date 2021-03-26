# Table of Contents

* [app.dao](#app.dao)
  * [Dao](#app.dao.Dao)
    * [run\_es\_query](#app.dao.Dao.run_es_query)

<a name="app.dao"></a>
# app.dao

<a name="app.dao.Dao"></a>
## Dao Objects

```python
class Dao(object)
```

<a name="app.dao.Dao.run_es_query"></a>
#### run\_es\_query

```python
 | run_es_query(data)
```

do an elasticsearch native query.

The query is expected to be in the elasticsearch search format.

**Returns**:

list of objects that match the query.


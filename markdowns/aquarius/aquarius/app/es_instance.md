---
title: es_instance
slug: aquarius/app/es_instance
app: aquarius
module: aquarius.app.es_instance
source: https://github.com/oceanprotocol/aquarius/blob/v3.1.2-62-g1ce2da0/aquarius/app/es_instance.py
version: 3.1.2
---
## ElasticsearchInstance

```python
class ElasticsearchInstance(object)
```

#### write

```python
 | def write(obj, resource_id=None)
```

Write obj in elasticsearch.

**Arguments**:

- `obj`: value to be written in elasticsearch.
- `resource_id`: id for the resource.

**Returns**:

id of the transaction.

#### read

```python
 | def read(resource_id)
```

Read object in elasticsearch using the resource_id.

**Arguments**:

- `resource_id`: id of the object to be read.

**Returns**:

object value from elasticsearch.

#### update

```python
 | def update(obj, resource_id)
```

Update object in elasticsearch using the resource_id.

**Arguments**:

- `obj`: new value
- `resource_id`: id of the object to be updated.

**Returns**:

id of the object.

#### delete

```python
 | def delete(resource_id)
```

Delete an object from elasticsearch.

**Arguments**:

- `resource_id`: id of the object to be deleted.

**Returns**:




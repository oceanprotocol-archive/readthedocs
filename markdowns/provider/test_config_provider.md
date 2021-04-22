---
title: test_config_provider
slug: /read-the-docs/provider/test_config_provider
app: provider
module: test.test_config_provider
---
#### test\_set\_config

```python
def test_set_config()
```

Tests that a custom config can be set on the ConfigProvider.

#### test\_metadataStoreUri\_config\_key

```python
def test_metadataStoreUri_config_key()
```

Tests that the metadata_cache_uri config property can be set using the
`metadataStoreUri` config dict key when created via the Ocean __init__

#### test\_metadataCacheUri\_config\_key

```python
def test_metadataCacheUri_config_key()
```

Tests that the metadata_cache_uri config property can be set using the
`metadataCacheUri` config dict key when created via the Ocean __init__

#### test\_config\_filename\_given\_file\_doesnt\_exist

```python
def test_config_filename_given_file_doesnt_exist()
```

Test creating a Config object.
Setup: filename given, file doesn't exist
Expect: complain

#### test\_config\_filename\_given\_file\_exists\_malformed\_content

```python
def test_config_filename_given_file_exists_malformed_content(monkeypatch, tmp_path)
```

Test creating a Config object.
Setup: filename given, file exists, malformed content
Expect: complain

#### test\_config\_filename\_given\_file\_exists\_wellformed\_content

```python
def test_config_filename_given_file_exists_wellformed_content()
```

Test creating a Config object.
Setup: filename given, file exists, content is well-formed
Expect: success

#### test\_config\_filename\_not\_given\_envvar\_is\_empty

```python
def test_config_filename_not_given_envvar_is_empty(monkeypatch)
```

Test creating a Config object.
Setup: filename not given, envvar is empty
Expect: complain

#### test\_config\_filename\_not\_given\_file\_doesnt\_exist

```python
def test_config_filename_not_given_file_doesnt_exist(monkeypatch)
```

Test creating a Config object.
Setup: filename not given, default file doesn't exist
Expect: complain

#### test\_config\_filename\_not\_given\_file\_exists\_malformed\_content

```python
def test_config_filename_not_given_file_exists_malformed_content(monkeypatch, tmp_path)
```

Test creating a Config object.
Setup: no filename given, default file exists, content is malformed
Expect: complain

#### test\_config\_filename\_not\_given\_file\_exists\_wellformed\_content

```python
def test_config_filename_not_given_file_exists_wellformed_content(monkeypatch)
```

Test creating a Config object.
Setup: filename not given, default file exists, content is well-formed
Expect: success. Uses config file at ENV_CONFIG_FILE.

#### test\_config\_from\_text\_wellformed\_content

```python
def test_config_from_text_wellformed_content()
```

Tests creating Config object.
Setup: from raw text, content is well-formed
Expect: success

#### test\_config\_from\_text\_malformed\_content

```python
def test_config_from_text_malformed_content()
```

Tests creating Config object.
Setup: from raw text, content is malformed
Expect: complain


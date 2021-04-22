---
title: test_data_service_provider
slug: /read-the-docs/provider/test_data_service_provider
app: provider
module: data_provider.test.test_data_service_provider
---
#### test\_set\_http\_client

```python
def test_set_http_client(with_nice_client)
```

Tests that a custom http client can be set on the DataServiceProvider.

#### test\_encryption\_fails

```python
def test_encryption_fails(with_evil_client)
```

Tests that asset encryption fails with OceanEncryptAssetUrlsError.

#### test\_nonce\_fails

```python
def test_nonce_fails(with_evil_client)
```

Tests that nonce retrieved erroneously is set to None.

#### test\_order\_requirements\_fails

```python
def test_order_requirements_fails(with_evil_client)
```

Tests failure of order requirements from endpoint.

#### test\_start\_compute\_job\_fails\_empty

```python
def test_start_compute_job_fails_empty(with_empty_client)
```

Tests failure of compute job from endpoint with empty response.

#### test\_start\_compute\_job\_fails\_error\_response

```python
def test_start_compute_job_fails_error_response(with_evil_client)
```

Tests failure of compute job from endpoint with non-200 response.

#### test\_send\_compute\_request\_failure

```python
def test_send_compute_request_failure(with_evil_client)
```

Tests failure of compute request from endpoint with non-200 response.

#### test\_compute\_job\_result

```python
def test_compute_job_result(with_nice_client)
```

Tests successful compute job starting.

#### test\_restart\_job\_result

```python
def test_restart_job_result(with_nice_client)
```

Tests successful compute job restart.

#### test\_delete\_job\_result

```python
def test_delete_job_result(with_nice_client)
```

Tests successful compute job deletion.

#### test\_invalid\_file\_name

```python
def test_invalid_file_name()
```

Tests that no filename is returned if attachment headers are found.

#### test\_expose\_endpoints

```python
def test_expose_endpoints()
```

Tests that the DataServiceProvider exposes all service endpoints.

#### test\_provider\_address

```python
def test_provider_address()
```

Tests that a provider address exists on the DataServiceProvider.

#### test\_provider\_address\_with\_url

```python
def test_provider_address_with_url()
```

Tests that a URL version of provider address exists on the DataServiceProvider.

#### test\_get\_root\_uri

```python
def test_get_root_uri()
```

Tests extraction of base URLs from various inputs.

#### test\_build\_endpoint

```python
def test_build_endpoint()
```

Tests that service endpoints are correctly built from URL and service name.

#### test\_build\_specific\_endpoints

```python
def test_build_specific_endpoints()
```

Tests that a specific list of agreed endpoints is supported on the DataServiceProvider.


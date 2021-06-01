---
title: service_factory
slug: ocean_lib/common/agreements/service_factory
app: ocean.py
module: ocean_lib.common.agreements.service_factory
source: https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/common/agreements/service_factory.py
version: 0.5.22
---
## ServiceDescriptor

```python
class ServiceDescriptor(object)
```

Tuples of length 2. The first item must be one of ServiceTypes and the second
item is a dict of parameters and values required by the service

#### metadata\_service\_descriptor

```python
 | @staticmethod
 | def metadata_service_descriptor(attributes, service_endpoint)
```

Metadata service descriptor.

**Arguments**:

- `attributes`: conforming to the Metadata accepted by Ocean Protocol, dict
- `service_endpoint`: identifier of the service inside the asset DDO, str

**Returns**:

Service descriptor.

#### authorization\_service\_descriptor

```python
 | @staticmethod
 | def authorization_service_descriptor(service_endpoint)
```

Authorization service descriptor.

**Arguments**:

- `service_endpoint`: identifier of the service inside the asset DDO, str

**Returns**:

Service descriptor.

#### access\_service\_descriptor

```python
 | @staticmethod
 | def access_service_descriptor(attributes, service_endpoint)
```

Access service descriptor.

**Arguments**:

- `attributes`: attributes of the access service, dict
- `service_endpoint`: identifier of the service inside the asset DDO, str
- `template_id`: 

**Returns**:

Service descriptor.

#### compute\_service\_descriptor

```python
 | @staticmethod
 | def compute_service_descriptor(attributes, service_endpoint)
```

Compute service descriptor.

**Arguments**:

- `attributes`: attributes of the compute service, dict
- `service_endpoint`: identifier of the service inside the asset DDO, str
- `template_id`: 

**Returns**:

Service descriptor.

## ServiceFactory

```python
class ServiceFactory(object)
```

Factory class to create Services.

#### build\_services

```python
 | @staticmethod
 | def build_services(service_descriptors)
```

Build a list of services.

**Arguments**:

- `service_descriptors`: List of tuples of length 2. The first item must be one of
ServiceTypes
and the second item is a dict of parameters and values required by the service

**Returns**:

List of Services

#### build\_service

```python
 | @staticmethod
 | def build_service(service_descriptor)
```

Build a service.

**Arguments**:

- `service_descriptor`: Tuples of length 2. The first item must be one of ServiceTypes
and the second item is a dict of parameters and values required by the service

**Returns**:

Service

#### build\_metadata\_service

```python
 | @staticmethod
 | def build_metadata_service(metadata, service_endpoint)
```

Build a metadata service.

**Arguments**:

- `metadata`: conforming to the Metadata accepted by Ocean Protocol, dict
- `service_endpoint`: identifier of the service inside the asset DDO, str

**Returns**:

Service

#### build\_authorization\_service

```python
 | @staticmethod
 | def build_authorization_service(attributes, service_endpoint)
```

Build an authorization service.

**Arguments**:

- `attributes`: attributes of authorization service, dict
- `service_endpoint`: identifier of the service inside the asset DDO, str

**Returns**:

Service

#### build\_access\_service

```python
 | @staticmethod
 | def build_access_service(attributes, service_endpoint)
```

Build an authorization service.

**Arguments**:

- `attributes`: attributes of access service, dict
- `service_endpoint`: identifier of the service inside the asset DDO, str

**Returns**:

ServiceAgreement instance

#### build\_compute\_service

```python
 | @staticmethod
 | def build_compute_service(attributes, service_endpoint)
```

Build an authorization service.

**Arguments**:

- `attributes`: attributes of compute service, dict
- `service_endpoint`: identifier of the service inside the asset DDO, str

**Returns**:

ServiceAgreement instance


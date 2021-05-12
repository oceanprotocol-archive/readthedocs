---
title: compute
slug: /read-the-docs/provider/compute
app: provider
module: routes.compute
---
#### computeDelete

```python
@services.route("/compute", methods=["DELETE"])
@validate(ComputeRequest)
def computeDelete()
```

Deletes a workflow.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: signature
    in: query
    description: Signature of the documentId to verify that the consumer has rights to download the asset.
    type: string
  - name: documentId
    in: query
    description: The ID of the asset
    required: true
    type: string
  - name: consumerAddress
    in: query
    description: The consumer address.
    required: true
    type: string
  - name: jobId
    in: query
    description: JobId.
    type: string
responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One of the required attributes is missing.
  401:
    description: Invalid asset data.
  503:
    description: Service Unavailable

#### computeStop

```python
@services.route("/compute", methods=["PUT"])
@validate(ComputeRequest)
def computeStop()
```

Stop the execution of a workflow.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: signature
    in: query
    description: Signature of (consumerAddress+jobId+documentId) to verify the consumer of
        this compute job/asset. The signature uses ethereum based signing method
        (see https://github.com/ethereum/EIPs/pull/683)
    type: string
  - name: documentId
    in: query
    description: The ID of the asset. If not provided, all currently running compute
        jobs will be stopped for the specified consumerAddress
    required: true
    type: string
  - name: consumerAddress
    in: query
    description: The consumer ethereum address.
    required: true
    type: string
  - name: jobId
    in: query
    description: The ID of the compute job. If not provided, all running compute jobs of
        the specified consumerAddress/documentId are suspended
    type: string
responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One of the required attributes is missing.
  401:
    description: Consumer signature is invalid or failed verification.
  503:
    description: Service unavailable

#### computeStatus

```python
@services.route("/compute", methods=["GET"])
@validate(UnsignedComputeRequest)
def computeStatus()
```

Get status for a specific jobId/documentId/owner

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: signature
    in: query
    description: Signature of (consumerAddress+jobId+documentId) to verify the consumer of
        this asset/compute job. The signature uses ethereum based signing method
        (see https://github.com/ethereum/EIPs/pull/683)
    type: string
  - name: documentId
    in: query
    description: The ID of the asset. If not provided, the status of all
        currently running and old compute jobs for the specified consumerAddress will be returned.
    required: true
    type: string
  - name: consumerAddress
    in: query
    description: The consumer ethereum address.
    required: true
    type: string
  - name: jobId
    in: query
    description: The ID of the compute job. If not provided, all running compute jobs of
        the specified consumerAddress/documentId are suspended
    type: string

responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One of the required attributes is missing.
  401:
    description: Consumer signature is invalid or failed verification.
  503:
    description: Service Unavailable

#### computeStart

```python
@services.route("/compute", methods=["POST"])
@validate(ComputeStartRequest)
def computeStart()
```

Call the execution of a workflow.

---
tags:
  - services
consumes:
  - application/json
parameters:
  - name: signature
    in: query
    description: Signature of (consumerAddress+jobId+documentId) to verify the consumer of
        this asset/compute job. The signature uses ethereum based signing method
        (see https://github.com/ethereum/EIPs/pull/683)
    type: string
  - name: consumerAddress
    in: query
    description: The consumer ethereum address.
    required: true
    type: string

  - name: algorithmDid
    in: query
    description: The DID of the algorithm Asset to be executed
    required: false
    type: string
  - name: algorithmMeta
    in: query
    description: json object that define the algorithm attributes and url or raw code
    required: false
    type: json string
  - name: output
    in: query
    description: json object that define the output section
    required: true
    type: json string
responses:
  200:
    description: Call to the operator-service was successful.
  400:
    description: One of the required attributes is missing.
  401:
    description: Consumer signature is invalid or failed verification
  503:
    description: Service unavailable


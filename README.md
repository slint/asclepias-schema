This repository contains the schemas for events, payloads and definitions.
**NOTE:** Do not modify this README.md file directly, it's a compiled file. Please modify the README.md.template and execute ``python build_docs.py > README.md``.

# Event, payload and definitions schemas
* [`Event schema`](#reference-event-schema) (root object `event`)
* [`Relation payload schema`](#reference-payload-relation-schema) (nested object under `event["payload"]`)
* [`Object payload schema`](#reference-payload-object-schema) (nested object under `event["payload"]`)
* [`Payload definitions`](#reference-payload-definitions-schema) (Object definitions used in payloads)


---------------------------------------
<a name="reference-event-schema"></a>
## Event schema

Schema of the event message.

**Properties**

|   |Type|Description|Required|
|---|----|-----------|--------|
| **event_type** | string | Type of the event. Controlled vocabulary: 'relation_created' or 'relation_deleted' | Yes |
| **creator** | string | Name of the part which emmited this event. | Yes |
| **source** | string | Name of the source, algorithm or procedure, which created this event. | Yes |
| **payload** | array | Payload information specific to the event_type. An array, containing one or more payloads of the structure matching with the event_type. | Yes |
| **id** | string | Globally unique identifier of the event (UUID version 4 as specified in RFC 4122). | Yes |
| **time** | string | Time when the payload information was created. | Yes |
| **description** | string | Free-text description of the event. | No |


Additional properties are allowed.

<a name="reference-payload-relation-schema"></a>
## Payload schema: Relation

Schema of the relation payload.

**Properties**

|   |Type|Description|Required|
|---|----|-----------|--------|
| **relation_publication_date** | string | Date of the relation publishing. | No |
| **relation_provider** | object ([`organization`](#definition-organization)) | Provider of the relation. | No |
| **relationship_type** | object ([`relationship`](#definition-relationship)) | Type of the relation. | No |
| **license_url** | string | URL to a license of the relation (recommended CC0) | Yes |
| **source** | object ([`object`](#definition-object)) | First object in the relation. | Yes |
| **target** | object ([`object`](#definition-object)) | Second object in the relation. | Yes |


Additional properties are allowed.

<a name="reference-payload-object-schema"></a>
## Payload schema: Object

Schema of the object payload.

**Properties**

|   |Type|Description|Required|
|---|----|-----------|--------|
| **object_publication_date** | string | Date when the information on this object was first published. | Yes |
| **object_provider** | object ([`organization`](#definition-organization)) | Entity providing the object event information. | Yes |
| **object** | object ([`object`](#definition-object)) | Information on the object . | Yes |
| **metadata** | object | Metadata that is associated with this object | No |
| **metadata_schema** | string | Example: DataCite, Zenodo | No |
| **metadata_schema_url** | string | Example: https://zenodo.org/schemas/records/record-v1.0.0.json | No |


Additional properties are allowed.

<a name="reference-payload-definitions-schema"></a>
## Payload definitions

Schemas of structured objects in ``definitions.json`` schema.

**Available ``definitions``**

### Definition: ``relationship``
<a name="definition-relationship"></a>

|   |Type|Description|Required|
|---|----|-----------|--------|
| **scholix_relationship** | string | Currently-supported Scholix relations. | No |
| **original_relationship_name** | string | All other relationship names. Supporting all metadata types of DataCite Metadata Schema 4.1 | No |
| **original_relationship_schema** | string | Schema of the relation type. Currently DataCite only. | No |

### Definition: ``organization``
<a name="definition-organization"></a>

|   |Type|Description|Required|
|---|----|-----------|--------|
| **name** | string | Name of the organization, which can be an event payload information provider, object publisher etc. | No |
| **identifier** | object ([`identifier`](#definition-identifier)) |  | No |

### Definition: ``object``
<a name="definition-object"></a>

|   |Type|Description|Required|
|---|----|-----------|--------|
| **identifier** | object ([`identifier`](#definition-identifier)) |  | No |
| **type** | object ([`object_type`](#definition-object_type)) |  | No |
| **publisher** | object ([`organization`](#definition-organization)) |  | No |
| **publication_date** | string | Object (PID) first publication date. Type dc:date. | No |

### Definition: ``identifier``
<a name="definition-identifier"></a>

|   |Type|Description|Required|
|---|----|-----------|--------|
| **id** | string | E.g.: 10.5281/zenodo.123 | Yes |
| **id_schema** | string | E.g.: DOI | Yes |
| **id_url** | string | E.g.: http://doi.org | No |

### Definition: ``object_type``
<a name="definition-object_type"></a>

|   |Type|Description|Required|
|---|----|-----------|--------|
| **name** | string |  | No |
| **sub_type** | string |  | No |
| **sub_type_schema** | string |  | No |



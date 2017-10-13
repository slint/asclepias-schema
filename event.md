# Schemas
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
| **relation_provider** |  | Provider of the relation. | No |
| **relationship_type** |  | Type of the relation. | No |
| **license_url** | string | URL to a license of the relation (recommended CC0) | Yes |
| **source** |  | First object in the relation. | Yes |
| **target** |  | Second object in the relation. | Yes |


Additional properties are allowed.

<a name="reference-payload-object-schema"></a>
## Payload schema: Object

Schema of the object payload.

**Properties**

|   |Type|Description|Required|
|---|----|-----------|--------|
| **object_publication_date** | string | Date when the information on this object was first published. | Yes |
| **object_provider** |  | Entity providing the object event information. | Yes |
| **object** |  | Information on the object . | Yes |
| **metadata** | object | Metadata that is associated with this object | No |
| **metadata_schema** | string | Example: DataCite, Zenodo | No |
| **metadata_schema_url** | string | Example: https://zenodo.org/schemas/records/record-v1.0.0.json | No |


Additional properties are allowed.

<a name="reference-payload-definitions-schema"></a>
## Payload definitions

Schema of the object payload.

**Available ``definitions``**

|   |Type|Description|Required|
|---|----|-----------|--------|
|**identifier**|`object`|Identifier of an object or organization.||
|**object_type**|`object`|Object type.||
|**relationship**|`object`|Relationship type.||
|**object**|`object`|Object.||
|**organization**|`string`|Organization.||

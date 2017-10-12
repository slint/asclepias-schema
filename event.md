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
|**event_type**|`string`|Describes the type of payload in this event. Controlled vocabulary: ``relation_created``, ``relation_deleted``, ``object_created`` or ``object_deleted``|Yes|
|**creator**|`string`|Name of the part which emmited this event.|Yes|
|**source**|`string`|Name of the source, algorithm or procedure, which created this event.|Yes|
|**id**|`string`|Globally unique identifier of the event (UUID version 4 as specified in RFC 4122).)|Yes|
|**time**|`string`|Time when the payload information was created.|Yes|
|**description**|`string`|Free-text description of the event.|No|
|**payload**|`array`|Array of structured objects, each of the same type specified in `event_type`, containing one or more event payloads.|Yes|

Additional properties are allowed.

<a name="reference-payload-relation-schema"></a>
## Payload schema: Relation

Schema of the relation payload.

**Properties**

|   |Type|Description|Required|
|---|----|-----------|--------|
|**relation_publication_date**|`string`|Date of the relation publishing|Yes|
|**relation_provider**|`object` (definitions/organization)|Name of the party which emmited this event.|Yes|
|**relationship_type**|`object` (definitions/relationship)|Name of the source, algorithm or procedure, which created this event.|Yes|
|**license_url**|`string`|URL to a license of the relation (recommended CC0)|Yes|
|**source**|`object` (definitions/object)|Source (first) object in the relation.|Yes|
|**target**|`object` (definitions/object)|Target (second) object in the relation.|Yes|

Additional properties are allowed.

<a name="reference-payload-object-schema"></a>
## Payload schema: Object

Schema of the object payload.

**Properties**

|   |Type|Description|Required|
|---|----|-----------|--------|
|**object_publication_date**|`string`|Date when the information on this object was first published.|Yes|
|**object_provider**|`object` (definitions/organization)|Name of the part which emmited this event.|Yes|
|**object**|`object` (definitions/object)|Source (first) object in the relation.|Yes|
|**metadata**|`object`|Metadata that is associated with this object.|No|
|**metadata_schema**|`string`|Schema of the metadata. Example: `DataCite`, `Zenodo`.|No|
|**metadata_schema_url**|`string`|URL containing the schema. Example: https://zenodo.org/schemas/records/record-v1.0.0.json |No|

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

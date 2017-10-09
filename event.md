# Objects
* [`Objects relation payload schema`](#reference-objects-relation-payload-schema) (root object)


---------------------------------------
<a name="reference-objects-relation-payload-schema"></a>
## Objects relation payload schema

Schema of the payload, describing the relations between objects.

**Properties**

|   |Type|Description|Required|
|---|----|-----------|--------|
|**link_publication_date**|`string`||Yes|
|**link_provider**|`any`||Yes|
|**relationship_type**|`any`||Yes|
|**license_url**|`string`|URL to a license of the link (recommended CC0)|Yes|
|**source**|`#definitions/object`||Yes|
|**target**|`#definitions/object`||Yes|

Additional properties are allowed.

### objects.relation.payload.schema.link_publication_date

* **Type**: `string`
* **Required**: No

### objects.relation.payload.schema.link_provider

* **Type**: `any`
* **Required**: No

### objects.relation.payload.schema.relationship_type

* **Type**: `any`
* **Required**: No

### objects.relation.payload.schema.license_url

URL to a license of the link (recommended CC0)

* **Type**: `string`
* **Required**: No

### objects.relation.payload.schema.source

* **Type**: `#definitions/object`
* **Required**: No

### objects.relation.payload.schema.target

* **Type**: `#definitions/object`
* **Required**: No

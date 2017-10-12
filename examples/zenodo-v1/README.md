# Example Zenodo Stories + Events

## Simple record workflow

1. User creates **[Record A]** with citations
    1. `object_created`
        1. [**DOI:10.5072/zenodo.10**](data/simple/1-object_created-1.json)
        1. [**DOI:10.5072/zenodo.11**](data/simple/1-object_created-2.json)
    1. [`relation_created`](data/simple/1-relation_created.json)
        1. **DOI:10.5072/zenodo.11** isIdenticalTo
           **URL:https://zenodo.org/record/11**
        1. **DOI:10.5072/zenodo.11** isPartOf **DOI:10.5072/zenodo.10**
        1. **DOI:10.5072/zenodo.11** cites **DOI:10.5072/zenodo.53155**
        1. **DOI:10.5072/zenodo.11** cites **DOI:10.5072/zenodo.56799**
1. User edits **[Record A]**, modifies title
    1. [`object_updated`](data/simple/2-object_updated.json) -
       **DOI:10.5072/zenodo.11**
1. User edits **[Record A]**, removes citations
    1. [`object_updated`](data/simple/3-object_updated.json) -
       **DOI:10.5072/zenodo.11**
    1. [`relation_deleted`](data/simple/3-relation_deleted.json)
        1. **DOI:10.5072/zenodo.11** cites **DOI:10.5072/zenodo.53155**

## Full record workflow

> TODO: Add event payloads

1. User creates **[Record B]** with citations
    1. `object_created`
        1. [**DOI:10.5072/zenodo.20**](data/full/1-object_created-1.json)
        1. [**DOI:10.5072/zenodo.21**](data/full/1-object_created-2.json)
    1. [`relation_created`](data/full/1-relation_created.json)
        1. **DOI:10.5072/zenodo.21** isIdenticalTo
           **URL:https://zenodo.org/record/21**
        1. **DOI:10.5072/zenodo.21** isPartOf **DOI:10.5072/zenodo.20**
        1. **DOI:10.5072/zenodo.21** cites **DOI:10.5072/zenodo.53155**
        1. **DOI:10.5072/zenodo.21** cites **DOI:10.5072/zenodo.56799**
1. User edits **[Record B]**, removes and adds citations
    1. [`object_updated`](data/full/2-object_updated.json) -
       **DOI:10.5072/zenodo.21**
    1. [`relation_deleted`](data/full/2-relation_deleted.json)
        1. **DOI:10.5072/zenodo.21** cites **DOI:10.5072/zenodo.53155**
    1. [`relation_created`](data/full/2-relation_created.json)
        1. **DOI:10.5072/zenodo.21** cites **DOI:10.5072/zenodo.887279**
1. Admin removes **[Record B]**
    1. `object_deleted`
        1. [**DOI:10.5072/zenodo.20**](data/full/3-object_deleted-1.json)
        1. [**DOI:10.5072/zenodo.21**](data/full/3-object_deleted-2.json)
    1. [`relation_deleted`](data/full/3-relation_deleted.json)
        1. **DOI:10.5072/zenodo.21** isIdenticalTo
           **URL:https://zenodo.org/record/21**
        1. **DOI:10.5072/zenodo.21** isPartOf **DOI:10.5072/zenodo.20**
        1. **DOI:10.5072/zenodo.21** cites **DOI:10.5072/zenodo.56799**
        1. **DOI:10.5072/zenodo.21** cites **DOI:10.5072/zenodo.887279**

## Record new version

> TODO: Add event payloads

1. User creates **[Record C]**
    1. `object_created`
        1. [**DOI:10.5072/zenodo.30**](data/version/1-object_created-1.json)
        1. [**DOI:10.5072/zenodo.31**](data/version/1-object_created-2.json)
    1. [`relation_created`](data/version/1-relation_created.json)
        1. **DOI:10.5072/zenodo.31** isIdenticalTo
           **URL:https://zenodo.org/record/31**
        1. **DOI:10.5072/zenodo.31** isPartOf **DOI:10.5072/zenodo.30**
1. User creates new version of **[Record C]**
    1. `object_created`
        1. [**DOI:10.5072/zenodo.32**](data/version/2-object_created.json)
    1. [`relation_created`](data/version/2-relation_created.json)
        1. **DOI:10.5072/zenodo.32** isIdenticalTo
           **URL:https://zenodo.org/record/32**
        1. **DOI:10.5072/zenodo.32** isPartOf **DOI:10.5072/zenodo.30**

## GitHub release

> TODO: Add event payloads

1. User creates release v1.0.0 on GitHub repository `dfm/corner.py`, which
   arrives on Zenodo, creating **[Record D]**
    1. `object_created`
        1. [**DOI:10.5072/zenodo.40**](data/github/1-object_created-1.json)
        1. [**DOI:10.5072/zenodo.41**](data/github/1-object_created-2.json)
    1. [`relation_created`](data/github/1-relation_created.json)
        1. **DOI:10.5072/zenodo.41** isIdenticalTo
           **URL:https://zenodo.org/record/41**
        1. **DOI:10.5072/zenodo.41** isPartOf **DOI:10.5072/zenodo.40**
        1. **DOI:10.5072/zenodo.41** isSupplementOf
           **URL:https://github.com/dfm/corner.py/tree/v1.0.0**
        1. **DOI:10.5072/zenodo.41** isIdenticalTo
           **URL:https://github.com/dfm/corner.py/tree/v1.0.0**
1. User creates release v1.1.0 on GitHub repository `dfm/corner.py`, which
   arrives on Zenodo, creating new version of **[Record D]**
    1. `object_created`
        1. [**DOI:10.5072/zenodo.42**](data/github/2-object_created.json)
    1. [`relation_created`](data/github/2-relation_created.json)
        1. **DOI:10.5072/zenodo.42** isIdenticalTo
           **URL:https://zenodo.org/record/42**
        1. **DOI:10.5072/zenodo.42** isPartOf **DOI:10.5072/zenodo.40**
        1. **DOI:10.5072/zenodo.42** isSupplementOf
           **URL:https://github.com/dfm/corner.py/tree/v1.1.0**
        1. **DOI:10.5072/zenodo.42** isIdenticalTo
           **URL:https://github.com/dfm/corner.py/tree/v1.1.0**

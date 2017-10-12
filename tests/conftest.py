import pytest
import os
import json


#
# JSON schema and test data loading fixtures
#
@pytest.fixture
def test_dir():
    return os.path.dirname(__file__)


@pytest.fixture
def data_dir(test_dir):
    return os.path.join(test_dir, 'data')


@pytest.fixture
def jsonschema_dir(test_dir):
    return os.path.join(test_dir, '..', 'jsonschema')


def load_schema(basedir, filename):
    with open(os.path.join(basedir, filename)) as fp:
        schema = json.load(fp)
    return schema


@pytest.fixture
def relation_schema(jsonschema_dir):
    return load_schema(jsonschema_dir, 'relation.json')


@pytest.fixture
def event_schema(jsonschema_dir):
    return load_schema(jsonschema_dir, 'event.json')


#
# Payload and events mocks loading (form JSON files)
#
@pytest.fixture
def zenodo_relation_events_dir():
    pass


#
# Raw relation payload and events examples
#
@pytest.fixture
def ads_relation_payloads():
    # Example from ADS
    obj = {
        "relationship_type": {
            "original_relationship_schema": "DataCite",
            "original_relationship_name": "Cites",
            "scholix_relationship": "References"
        },
        "target": {
            "Identifier": {
                "id": "10.5281/zenodo.11020",
                "id_schema": "DOI",
                "id_url": "https://doi.org"
            },
            "type": {
                "name": "software"
            }
        },
        "source": {
            "identifier": {
                "id": "2016ApJ...818..156C",
                "id_schema": "bibcode",
                "id_url": "http://adsabs.harvard.edu/abs/"
            }
        },
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
    }

    return obj


@pytest.fixture
def minimal_relation_event():
    """Minimal event."""
    obj = {
        "id": "d969a56d-e520-405d-a24f-497ac6923781",
        "description": "ADS citation events",
        "creator": "ADS",
        "source": "ADS.Discovery",
        "time": "1441166640.359496",
        "event_type": "relation_created",
        "payload": [{
            "relationship_type": {
                "original_relationship_schema": "DataCite",
                "original_relationship_name": "Cites",
                "scholix_relationship": "References"
            },
            "target": {
                "Identifier": {
                    "id": "10.5281/zenodo.11020",
                    "id_schema": "DOI",
                    "Id_url": "https://doi.org"
                },
                "type": {
                    "name": "software"
                }
            },
            "source": {
                "identifier": {
                    "id": "2016ApJ...818..156C",
                    "id_schema": "bibcode",
                    "Id_url": "http://adsabs.harvard.edu/abs/"
                }
            },
            "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
        }]
    }

    return obj

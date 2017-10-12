"""Test object events against the JSONSchema."""
from jsonschema import validate


def test_zenodo_object_events(zenodo_object_events, event_schema):
    """Test Zenodo object event JSONSchema validation."""
    # Will rase in case of schema validation errors
    for data in zenodo_object_events:
        validate(data, event_schema)

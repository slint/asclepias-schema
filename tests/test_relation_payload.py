"""Test relation payloads against the JSONSchema."""
from jsonschema import validate


def test_ads_relation_payloads(ads_relation_payloads, relation_schema):
    """Test simple relation payload JSONSchema validation."""
    # Will rase in case of schema validation errors
    for data in ads_relation_payloads:
        validate(data, relation_schema)

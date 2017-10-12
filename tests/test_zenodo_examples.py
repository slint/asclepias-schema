"""Test Zenodo example events against the JSONSchema."""
import json
from glob import glob

from jsonschema import validate


def test_event_payloads(zenodo_examples_data_dir, event_schema):
    """Test if Zenodo events are validated by the event JSONSchema."""
    event_files = glob(u'{}/**/*.json'.format(zenodo_examples_data_dir))
    for f in event_files:
        with open(f) as fp:
            validate(json.load(fp), event_schema)

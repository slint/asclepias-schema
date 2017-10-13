import os
import jinja2
import json
from collections import OrderedDict


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


schemas = [
    ('event', 'event.json'),
    ('relation', 'relation.json'),
    ('object', 'object.json'),
]

context = {}
for key, filename in schemas:
    with open('jsonschema/' + filename, 'r') as fp:
        data = json.load(fp, object_pairs_hook=OrderedDict)
        required = data['required']
        properties = data['properties']
        for k, v in properties.items():
            properties[k]['required'] = 'Yes' if k in required else 'No'
        context[key] = properties

with open('jsonschema/definitions.json', 'r') as fp:
    data = json.load(fp, object_pairs_hook=OrderedDict)
    definitions = data['definitions']
    context['definitions'] = {}
    for def_k, def_v in definitions.items():
        required = def_v.get('required', [])
        properties = def_v['properties']
        for k, v in properties.items():
            properties[k]['required'] = 'Yes' if k in required else 'No'
        context['definitions'][def_k] = properties

print(render('./README.md.template', context))

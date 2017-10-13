import os
import jinja2
import json


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
        data = json.load(fp)
        required = data['required']
        properties = data['properties']
        for k, v in properties.items():
            properties[k]['required'] = 'Yes' if k in required else 'No'
        context[key] = properties

print(render('./event.md.tmp', context))

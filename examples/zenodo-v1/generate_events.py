import os
from copy import deepcopy
from io import BytesIO

import requests

BASE_URL = os.environ.get('ZENODO_BASE_URL', 'http://localhost:5000')
# ACCESS_TOKEN = os.environ.get('ZENODO_ACCESS_TOKEN', 'CHANGEME')

# XXX: REMOVE
ACCESS_TOKEN = '6ulGoOcEqvN7gGytSfdkzdNyEKApSxDEy3oL3NSx2IUdudjpAn8hQorqxf0R'
# XXX: REMOVE

session = requests.Session()
session.params = {'access_token': ACCESS_TOKEN}


TRANSFERED_FIELDS = [
    'title',
    'upload_type',
    'publication_type',
    'access_right',
    'license',
    'description',
    'creators',
    'related_identifiers',
]


DATA_TEMPLATE = {
    'metadata': {
        'title': 'Record A',
        'access_right': 'open',
        'license': 'cc-by-sa',
        'upload_type': 'publication',
        'publication_type': 'article',
        'description': 'Test Record A',
        'creators': [{'name': 'Doe, John', 'affiliation': 'Zenodo'}],
    }
}


def publish_record(data=None, filename=None, file_content=None):
    req_data = deepcopy(DATA_TEMPLATE)
    req_data.update(data or {})

    # Create a deposit
    url = '{}/api/deposit/depositions'.format(BASE_URL)
    res = session.post(url, json=req_data)
    links = res.json()['links']
    files_url = links['bucket']
    publish_url = links['publish']

    # Upload a file
    data = BytesIO(file_content.encode('utf8') or b'# Record A article')
    url = files_url + '/{}'.format(filename or 'record-a.md')
    res = session.put(url, data=data)

    # Publish
    res = session.post(publish_url)
    return res.json()


def edit_record(depid, data=None):
    url = '{}/api/deposit/depositions/{}/actions/edit'.format(BASE_URL, depid)
    res = session.post(url)
    res_data = res.json()
    links = res_data['links']
    deposit_url = links['self']
    publish_url = links['publish']

    if data:
        req_data = {k: v for k, v in deepcopy(res_data['metadata'])
                    if k in TRANSFERED_FIELDS}
        req_data.update(data)
        res = session.put(deposit_url, json=req_data)
    res = session.post(publish_url)
    return res.json()


def new_record_version(depid, data=None, filename=None, file_content=None):
    # Create new version
    url = '{}/api/deposit/depositions/{}/actions/newversion'.format(
        BASE_URL, depid)
    res = session.post(url)
    links = res.json()['links']
    latest_draft_url = links['latest_draft']

    res = session.get(latest_draft_url)
    res_data = res.json()
    links = res_data['links']
    if data:
        data = deepcopy(res_data['metadata']).update(data)
        res = session.put()


if __name__ == '__main__':
    publish_record()

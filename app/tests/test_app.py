import json
from app import app


client = app.test_client()


def test_root():
resp = client.get('/')
assert resp.status_code == 200
data = json.loads(resp.data)
assert data['message'].startswith('Hola')

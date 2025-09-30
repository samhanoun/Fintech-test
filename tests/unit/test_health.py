import os
import sys
import pytest

# Ensure 'app_bank' is on sys.path so we can import top-level 'app' module as in runtime
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
APP_DIR = os.path.join(REPO_ROOT, 'app_bank')
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

from app import create_app  # noqa: E402


@pytest.fixture()
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.test_client() as client:
        yield client


def test_health_ok(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get('status') == 'ok'

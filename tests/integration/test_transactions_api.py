import os
import time

import requests


BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')


def wait_for_service(url: str, timeout: float = 30.0):
    start = time.time()
    last_err = None
    while time.time() - start < timeout:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                return True
        except Exception as e:
            last_err = e
        time.sleep(1)
    if last_err:
        raise RuntimeError(f"Service not ready after {timeout}s: {last_err}")
    raise RuntimeError(f"Service not ready after {timeout}s")


def test_health_endpoint():
    health_url = f"{BASE_URL}/health"
    wait_for_service(health_url, timeout=30)
    r = requests.get(health_url, timeout=2)
    assert r.status_code == 200
    assert r.json().get('status') == 'ok'

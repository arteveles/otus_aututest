import requests


def test_check_status(base_url, base_status_code):
    assert requests.get(url=base_url).status_code == base_status_code




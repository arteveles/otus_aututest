import pytest
import requests
import requests as requests

from lesson_4.jsonplaseholder.schemas import JustGet, ListGet, CreatePost
from lesson_4.logic.baseclasses.responses_validation import Responses
from lesson_4.logic.schemas.returned_schemas import PAGE_GET_JPH, PAGE_LISTING_JPH
from lesson_4.logic.schemas.returned_schemas import PAGE_CREATE, JSON_PC, PAREMETERS_PC
from lesson_4.logic.schemas.returned_schemas import PAGE_PUT, JSON_PP, PARAMETERS_PP, URL_JPH


def test_get():
    r = requests.get(url=PAGE_GET_JPH)
    print(r.json())
    request = Responses(r)
    request.assert_status_code(200).validate_pdt(JustGet)


def test_list():
    r = requests.get(url=PAGE_LISTING_JPH)
    request = Responses(r)
    request.assert_status_code(200).validate_pdt(ListGet)


def test_create():
    r = requests.post(url=PAGE_CREATE, json=JSON_PC, params=PAREMETERS_PC)
    request = Responses(r)
    request.assert_status_code(201).validate_pdt(CreatePost)


def test_put():
    r = requests.put(url=PAGE_PUT, json=JSON_PP, params=PARAMETERS_PP)
    request = Responses(r)
    request.assert_status_code(200).validate_pdt(CreatePost)


@pytest.mark.parametrize('urls', (
        '/posts/1/comments',
        '/albums/1/photos'
))
def test_check_route(urls):
    r = requests.get(url=URL_JPH + urls)
    response = Responses(r)
    response.assert_status_code(200)

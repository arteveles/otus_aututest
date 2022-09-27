import pytest
import requests
from lesson_4.logic.baseclasses.responses_validation import Responses
from lesson_4.configuration import OPEN_URL, OPEN_URL_OUTSLASH
from lesson_4.logic.schemas.returned_schemas import SINGLE_MADTREE, PAGE_NUMBER, STATES, CITY, COUNT_VALUES, PER_PAGE, \
    RESPONSE_STATES, SEARCH_URL, SEARCH_VALUE, AUTOCOMPLETE_RESPONSE, AUTOCOMPLETE_URL


class TestOpenBrew:

    def test_madtree_brewing_cincinnati(self):
        r = requests.get(url=OPEN_URL + f"madtree-brewing-cincinnati")
        response = Responses(r)
        response. \
            assert_status_code(200). \
            validate_single_openbrew(SINGLE_MADTREE)

    @pytest.mark.parametrize("per_page", PAGE_NUMBER)
    @pytest.mark.parametrize("count_values", COUNT_VALUES)
    def test_list_of_breweries(self, per_page, count_values):
        r = requests.get(url=OPEN_URL_OUTSLASH + f"{per_page}")
        response = Responses(r)
        response. \
            assert_status_code(200)
        assert len(response.response_json) == count_values

    @pytest.mark.parametrize("by_states", STATES)
    @pytest.mark.parametrize("city", CITY)
    def test_list_of_state(self, by_states, city):
        r = requests.get(url=OPEN_URL_OUTSLASH + f"{by_states}" + f"{city}" + f"{PER_PAGE}")
        response = Responses(r)
        response.assert_status_code(200)

    def test_search(self):
        r = requests.get(url=SEARCH_URL)
        response = Responses(r)
        response.assert_status_code(200)
        assert r.json()[0]["id"] == SEARCH_VALUE

    def test_autocomplete(self):
        r = requests.get(url=AUTOCOMPLETE_URL)
        response = Responses(r)
        response. \
            assert_status_code(200)
        assert r.json() == AUTOCOMPLETE_RESPONSE

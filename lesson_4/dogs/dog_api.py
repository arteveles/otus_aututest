import pytest
import requests
from lesson_4.dogs.baseclasses.responses_validation import Responses
from lesson_4.configuration import DOG_URL, DOG_URL_BREED
from lesson_4.dogs.schemas.returned_schemas import NAMES, ALL_BREEDS, RANDOM_DOG_IMG, ALL_BREED_IMG, SUB_BREAD, \
    SEND_BREAD


class TestDogAPI:

    def test_all_breads(self):
        r = requests.get(url=DOG_URL + f"list/all")
        response_all_breads = Responses(r)
        response_all_breads. \
            assert_status_code(200). \
            validate_test_all_breads(ALL_BREEDS)
        print(response_all_breads.response_json)

    def test_random_dog_img(self):
        r = requests.get(url=DOG_URL + f"image/random")
        response_random_dog_img = Responses(r)
        response_random_dog_img \
            .assert_status_code(200) \
            .validate_random_dog_img(RANDOM_DOG_IMG)
        print(response_random_dog_img.response_json)

    def test_all_bread_img(self):
        r = requests.get(url=DOG_URL_BREED + f"hound/images")
        response_all_bread_img = Responses(r)
        response_all_bread_img \
            .assert_status_code(200) \
            .validate_test_all_breads(ALL_BREED_IMG)
        print(response_all_bread_img.response_status)

    @pytest.mark.parametrize("hound", ["australian", "bulldog"])
    def test_sub_bread(self, hound):
        r = requests.get(url=DOG_URL_BREED + f"{hound}/list")
        response_sub_bread = Responses(r)
        response_sub_bread \
            .assert_status_code(200) \
            .validate_test_all_breads(SUB_BREAD)

    @pytest.mark.parametrize("names", NAMES)
    def test_send_bread(self, names):
        r = requests.get(url=DOG_URL_BREED + f"{names}/images/random")
        print(r.json())
        response_send_bread = Responses(r)
        response_send_bread \
            .assert_status_code(200).validate_send_bread(SEND_BREAD)
        print(response_send_bread.response_status)

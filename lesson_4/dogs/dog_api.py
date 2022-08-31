import requests
from lesson_4.dogs.baseclasses.responses import Responses
from lesson_4.configuration import DOG_URL
from lesson_4.dogs.schemas.returned_schemas import NAMES, ALL_BREEDS, RANDOM_DOG_IMG


class TestDogAPI:

    def test_all_breads(self):
        r = requests.get(url=DOG_URL + f"list/all")
        response_all_breads = Responses(r)
        response_all_breads.assert_status_code(200).validate_test_all_breads(ALL_BREEDS)
        print(response_all_breads.response_json)

    def test_random_dog_img(self):
        r = requests.get(url=DOG_URL + "image/random")
        response_random_dog_img = Responses(r)
        response_random_dog_img.assert_status_code(200).validate_random_dog_img(RANDOM_DOG_IMG)
        print(response_random_dog_img.response_json)


    def test_all_bread_img(self):
        response = requests.get(url=DOG_URL + "hound/images")

    def test_sub_bread(self):
        response = requests.get(url=DOG_URL + "hound/list")

    def test_send_bread(self):
        response = requests.post(url=DOG_URL + f"{NAMES}/images/random")

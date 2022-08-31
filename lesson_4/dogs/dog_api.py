import pytest
import requests


class TestDogAPI:
    URL = "https://dog.ceo/api/breeds/"
    breads_list = [
        ("african"),
        ("akita"),
        ("dingo")
    ]

    def test_all_breads(self):
        response = requests.get(f"{TestDogAPI.URL}+list/all")

    def test_random_dog_img(self):
        response = requests.get(f"{TestDogAPI.URL}+image/random")

    def test_all_bread_img(self):
        response = requests.get(f"{TestDogAPI.URL}+hound/images")

    def test_sub_bread(self):
        response = requests.get(f"{TestDogAPI.URL}+hound/list")

    @pytest.mark.parametrize('breed', breads_list)
    def test_send_bread(self, breed):
        response = requests.post(f"https://dog.ceo/api/breed/{breed}/images/random")

from jsonschema import validate
from lesson_4.dogs.enums.global_enums import GlobalErrorMessages


class Responses:

    def __init__(self, response_all_breads):
        self.response_all_breads = response_all_breads
        self.response_json = response_all_breads.json()
        self.response_status = response_all_breads.status_code

    def validate_test_all_breads(self, schema_all_breads):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_all_breads)
            else:
                validate(self.response_json, schema_all_breads)

    def validate_random_dog_img(self, schema_random_dog_img):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_random_dog_img)
            else:
                validate(self.response_json, schema_random_dog_img)

    def validate_all_bread_img(self, schema_all_bread_img):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_all_bread_img)
            else:
                validate(self.response_json, schema_all_bread_img)

    def validate_sub_bread(self, schema_sub_bread):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_sub_bread)
            else:
                validate(self.response_json, schema_sub_bread)

    def validate_send_bread(self, schema_send_bread):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_send_bread)
            else:
                validate(self.response_json, schema_send_bread)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

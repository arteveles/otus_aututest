from jsonschema import validate
from lesson_4.logic.enums.global_enums import GlobalErrorMessages


class Responses:

    def __init__(self, response_all):
        self.response_all = response_all
        self.response_json = response_all.json()
        self.response_status = response_all.status_code

    """validation for dog api"""

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

    """validation for openbrew api"""

    def validate_single_openbrew(self, schema_single_openbrew):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_single_openbrew)
            else:
                validate(self.response_json, schema_single_openbrew)

    def validate_list_of_breweries(self, schema_list_of_breweries):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_list_of_breweries)
            else:
                validate(self.response_json, schema_list_of_breweries)

    def validate_brew_by_state(self, schema_brew_by_state):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_brew_by_state)
            else:
                validate(self.response_json, schema_brew_by_state)

    def validate_autocomplete(self, schema_autocomplete):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema_autocomplete)
            else:
                validate(self.response_json, schema_autocomplete)

    """Jsonplaceholder pydantic validator"""

    def validate_pdt(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

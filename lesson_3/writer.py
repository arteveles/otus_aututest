import json
from reader import result


def write_to_result():
    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4)

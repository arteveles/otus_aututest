import json

from reader import ReadData, result


class WriteData(ReadData):

    @property
    def write_to_result(self):
        f = ReadData.file
        with open('result.json', 'w') as f:
            json.dump(result, f, indent=4)


print(result)

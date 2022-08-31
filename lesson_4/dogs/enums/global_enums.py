from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Получен неожиданный статус код"
    WRONG_RES_ALL_BREAD = "Неожиданное тело запроса"
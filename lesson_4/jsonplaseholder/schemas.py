from pydantic import validator, BaseModel, Field



class JustGet(BaseModel):
    userId: int
    id: int
    title: str
    body: str

    @validator("id")
    def validate_id(cls, v):
        if v > 1:
            raise ValueError("Id-шник не корректный")
        return v


class ListGet(BaseModel):
    userId: int
    id: int
    title: str
    body: str

    @validator("userId")
    def validate_userid(cls, v):
        if not v:
            raise ValueError("Отсутствует userId")
        return v

class CreatePost(BaseModel):
    title: str
    body: str
    userId: int
    id: int

    @validator("title")
    def validate_title(cls, v):
        if v != "foo":
            raise ValueError("Check title, it is not valid value")
        return v



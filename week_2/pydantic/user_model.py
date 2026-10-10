from pydantic import BaseModel, ValidationError


class User(BaseModel):
    name: str
    age: int
    email: str


try:
    User(name=123, age="not an integer", email="sam@example.com")
except ValidationError as error:
    print(error)
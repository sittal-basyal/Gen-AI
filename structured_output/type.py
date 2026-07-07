from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

person1 : Person ={
    "name": "John Doe",
    "age": 30,
    "email": "123@gmail.com"
}
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


# class User(BaseModel):
#     name: str = Field(..., min_length=2, max_length=50)
#     age: int = Field(..., gt=0, lt=120)
#     city: str = Field(..., min_length=2, max_length=50)


# @app.post("/create-user")
# def create_user(user:User):
#     return {
#         "message": f"User with name {user.name} of the age : {user.age} living in the city {user.city} is created succesfully ",
#         "data": user
#         }




# Nested examples of pydnantic models

class Address(BaseModel):
    city: str = Field(..., min_length=2, max_length=50)
    pincode: int = Field(..., gt=0, lt=999999)


class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    address: Address


@app.post("/create-user")
def create_user(user: User):
    return {
        "message": f"User with name {user.name} of the age : {user.age} living in the city {user.address.city} with pincode {user.address.pincode} is created succesfully ",
        "data": user
    }
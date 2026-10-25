from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

# let's learn about how we can implement the path , query and body parameters together in a single api endpoint

users = [] # we will store the user data in this list


class User(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    city: str = Field(min_length=2, max_length=50)


@app.post("/users")
def create_user(user:User):
    users.append(user)
    return{
        "message":"The user is created succesfully",
        "data":user
    }


@app.get("/users")
def get_users():
    return{
        "message":"The users are retrieved successfully",
        "data":users
    }


@app.put("/users/{user_id}")
def updated_user(user_id:int, user:User, notify:bool = False):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[index] = user
            return{
                "message":"The user is updated successfully",
                "data":user,
                "notify":notify
            }
    return{
        "message":"User not found"
    }
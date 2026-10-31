from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    password: str = Field(..., min_length=6, max_length=20)


class UserResponse(BaseModel):
    id: int
    name: str
    age: int


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return{
        "id": user_id,
        "name": "John Doe",
        "age": 30,
        "password":12345
    }

# because of response model we are not returning the password in the response 
# as you can see in the code the response_model = UserResponse which doesn't include the password
# , so it will not be shown in the swagger response as well
from fastapi import FastAPI
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    city: str = Field(..., min_length=2, max_length=50)

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Hey there, hello world"}



# CREATE A USER 


@app.post("/create-user")
def create_user(name: str, age: int, city: str):
    return {"message": f"User with name {name} of the age : {age} living in the city {city} is created succesfully "} 



# Another example of post request with pydantic model

@app.post("/create-user-2")
def create_user_2(user: User):
    return{
        "message":"User Created",
        "data":user
    }
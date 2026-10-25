from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

# let's learn about status codes and how we can use them in our api endpoints

# class User(BaseModel):
#     id: int = Field(..., gt=0)
#     name: str = Field(..., min_length=2, max_length=50)
#     age: int = Field(..., gt=0, lt=120)
#     city: str = Field(min_length=2, max_length=50)


# # Create api 


# @app.post("/users", status_code=status.HTTP_201_CREATED)
# def create_user(user: User):
#     return {
#         "response": status.HTTP_201_CREATED,
#         "message": "User created successfully",
#         "data": user
#     }


# # Custom response

# @app.get("/users")
# def get_users():
#     users = [
#         {"id": 1, "name": "John Doe", "age": 30, "city": "New York"},
#         {"id": 2, "name": "Jane Smith", "age": 25, "city": "Los Angeles"},
#         {"id": 3, "name": "Bob Johnson", "age": 35, "city": "Chicago"}
#     ]
#     return {
#         "response": "Success",
#         "message": "Users retrieved successfully",
#         "data": users
#     }


# # Error handling
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id <= 0:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID")
#     if user_id > 3:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     if user_id == 2:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
#     if user_id == 3:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
#     # Simulate fetching a user from a database
#     user = {"id": user_id, "name": "John Doe", "age": 30, "city": "New York"}
#     return {
#         "response": "Success",
#         "message": "User retrieved successfully",
#         "data": user
#     }


#_____________________________________________________________________________________________________________________________

# Advance concept 


@app.get("/users/{users_id}")
def get_users(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail= "User Not Found"
        )
    return{
        "id":1,
        "Name":"Shiv"
    }
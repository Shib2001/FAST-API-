from itertools import count

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Hey there, hello world"}


# Users Route 

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
            {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"},
            {"id": 3, "name": "Bob Johnson", "email": "bob.johnson@example.com"}
        ],

        "message": "Users retrieved successfully"
    }



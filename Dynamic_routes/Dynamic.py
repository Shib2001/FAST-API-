from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Hey there, hello world"}


#dyanmic routes

@app.get("/users/{user_id}")
def users(user_id: int): # ye yaha integrer string koi bhi data types uss dynamic routes ki id ko accept kar sakta hai
    return {"message": f"User with ID {user_id} retrieved successfully"}
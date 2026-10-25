from fastapi import FastAPI

app = FastAPI()


# User route

@app.get("/users")
def get_users(name: str = "John Doe", age: int = 0, city: str = None):
    #None here is used to say that city params is optional
    # for default values bss equal to me woh value daal de 
    return {"message": f"User with name {name} of the age : {age} living in the city {city} is retrvieed succesfully "}
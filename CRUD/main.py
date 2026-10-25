from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# Let's make a todo app with crud operations

todos = [] # idhar hum list ko intially store krwayeneg , so ye humne empty array define kr diya for that 

class Todo(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    completed: bool = Field(default=False)



# CREATE API 


@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Todo created successfully",
        "data": todo # we wrote this here because we want to return the data of the todo that we created successfully , and it will show on the swagger response as well
    } 


# GET API 


@app.get("/todos")
def get_todos():
    return {
        "message": "Todos retrieved successfully",
        "data": todos
    }


# GET BY ID API

@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {
                "message": "Todo retrieved successfully",
                "data": todo
            }
    return {
        "message": "Todo not found"
    } 


# UPDATE API by id 

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos): #enumerate() gives you two things together: 1. index → the position of the item in the list. 2. todo → the actual item stored at that position.
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully",
                "data": updated_todo
            }
    return {
        "message": "Todo not found"
    }


# UPDATE API by id with PATCH method

@app.patch("/todos/{todo_id}")
def update_todo_patch(todo_id: int, updated_fields: dict):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo = todo.copy(update=updated_fields)
            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully",
                "data": updated_todo
            }
    return {
        "message": "Todo not found"
    }


# DELETE API
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index) # pop() method removes the item at the specified position in the list, and returns it. 
            return {
                "message": "Todo deleted successfully",
                "data": deleted_todo
            }
    return {
        "message": "Todo not found"
    }
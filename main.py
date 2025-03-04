from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# Ger all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single todo 
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"messsage": "No todos found"}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo) 
    return {"message": "todo has been added"}

# Update a todo 
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"messsage": "No todos found found to upfate"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been Deleted"}
    return {"messsage": "No todos found"}
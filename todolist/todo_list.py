import os
import json

TODO_LIST_FILE = 'todo.json'

#loading our json data
def upload_todo_list():
    if os.path.exists(TODO_LIST_FILE):
        with open(TODO_LIST_FILE, 'r') as rf:
            return json.load(rf)
    else:
        return []

def list_todos(list_of_todo):
    for i, todo in enumerate(list_of_todo, 1):
        status = 'Done' if todo['done'] else 'Not Done'
        print(f"{i}. {todo['task']} [{status}]")
        
todos = upload_todo_list()
list_todos(todos)
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
    print('No  Task   status')
    for i, todo in enumerate(list_of_todo, 1):
        status = 'Done' if todo['Done'] else 'Not Done'
        print(f"{i}. {todo['Task']} [{status}]")

def add_todo_task():
    task = input("Enter the tasks you have: ")
    list_of_todo = upload_todo_list()
    list_of_todo.append({"Task": task, "Done": False}) 
    save_todo_task(list_of_todo)
    print('Task added sucessfully!')

def save_todo_task(list_of_todo):
    with open(TODO_LIST_FILE, 'w') as wf:
        json.dump(list_of_todo, wf, indent=3)



add_todo_task()
todos = upload_todo_list()
list_todos(todos)

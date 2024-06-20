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
def marks_task_done():
    list_of_todo = upload_todo_list()
    list_todos(list_of_todo)
    task_number = int(input("Enter teh task number you want to marks as one: ")) - 1
    if task_number > 0 and task_number < len(list_of_todo):
        list_of_todo[task_number]['Done'] = True
        save_todo_task(list_of_todo)
        print(f"Task Marked as done")

def main():
    while True:
        print("Select \n1.To view tasks in the list: \n2.To add task to the list: \n3.To mark a task as done\n0.To exit: ")
        choice = int(input("Choice: "))

        if choice == 1:
            list_of_todo = upload_todo_list()
            list_todos(list_of_todo)
        elif choice == 2:
            add_todo_task()
        elif choice == 3:
            marks_task_done()
        elif choice == 0:
            break


if __name__ == '__main__':
    main()

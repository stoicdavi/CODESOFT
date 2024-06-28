import os
import json

TODO_LIST_FILE = 'todo.json'

#loading our json data
def upload_todo_list():
    """
        Opens the file as rf in a read mode, and uploads its data in json format to rf
    """
    if os.path.exists(TODO_LIST_FILE):
        with open(TODO_LIST_FILE, 'r') as rf:
            return json.load(rf)
    else:
        return []

def list_todos(list_of_todo):
    """
        Displays the list of todos
    """
    print('\nNo  Task   status')
    for i, todo in enumerate(list_of_todo, 1):
        status = 'Done' if todo['Done'] else 'Not Done'
        print(f"{i}. {todo['Task']} [{status}]")

def add_todo_task():
    """"
        Allows a user to add a task to his/her to do list
    """
    while True:
        task = input("Enter the task you have: ").strip()
        if task == '':
            print('Task cannot be empty! please check and try adding again !')
            continue
        list_of_todo = upload_todo_list()
        list_of_todo.append({"Task": task, "Done": False}) 
        save_todo_task(list_of_todo)
        print(f'Task {task} added successfully!\n')
        
        while True:
            choice = input("Would you like to add another task? (Yes or No): ").strip().lower()
            if choice in ['yes', 'y']:
                break  
            elif choice in ['no', 'n']:
                return 
            else:
                print("Invalid choice, please enter 'Yes' or 'No'.")
              
              
def save_todo_task(list_of_todo):
    """
        Allow user to Saved the added task 
    """
    with open(TODO_LIST_FILE, 'w') as wf:
        json.dump(list_of_todo, wf, indent=3)
def marks_task_done():
    """
        Allows user to mark a task as done
    """
    list_of_todo = upload_todo_list()
    list_todos(list_of_todo)
    task_number = int(input("Enter the task number you want to marks as one: ")) - 1
    done_task1 = list_of_todo[task_number]['Done']
    if done_task1 == True:
        print("Task already marked done")
    else:
        if task_number > 0 and task_number < len(list_of_todo):
                    
            done_task = list_of_todo[task_number]['Done'] = True
            save_todo_task(list_of_todo)
            print(f"Task {done_task['Task']}Marked as done")
        else:
            print('Invalid Task number!')
    
def delete_task():
    """
        Allow a user to delete a task
    """
    while True:
        list_of_todo = upload_todo_list()
        list_todos(list_of_todo)
        
        if not list_of_todo:
            print("No tasks to delete.")
            break
        
        task_number = int(input('Enter the task number you want to delete (or 0 to exit): ')) - 1
        
        if task_number == -1:
            break  # Exit the loop if the user enters 0
        elif task_number >=0 and task_number < len(list_of_todo):
            deleted_task = list_of_todo.pop(task_number)
            save_todo_task(list_of_todo)
            print(f"Task '{deleted_task['Task']}' successfully deleted!\n")
        else:
            print('Invalid task number. Please check and try again!')
            continue
        
        choice = input("Would you like to delete another task? (Yes or no)").lower()
        if choice not in ['yes', 'y']:
            break
        elif choice in ['no', 'n']:
            return 
        else:
            print("Invalid choice, please enter 'Yes' or 'No'.")

        if not list_of_todo:
            print("All tasks have been deleted.")
            break


def main():
    print("**Welcome to DeANTECH Todo List!**")
    while True:
       
        print("Select \n1.To view tasks in the list: \n2.To add a task to the list: ")
        print("3.To mark a task as done\n4.To delete a task from the list \n0.To exit: ")
        choice = int(input("Choice: "))

        if choice == 1:
            list_of_todo = upload_todo_list()
            list_todos(list_of_todo)
        elif choice == 2:
            add_todo_task()
        elif choice == 3:
            marks_task_done()
        elif choice == 4:
            delete_task()
        elif choice == 0:
            break


if __name__ == '__main__':
    main()

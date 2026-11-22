from linked import *
from task_queue import *
from storagetion import *


def save_data():
    tasks = get_all_tasks()
    save_tasks(tasks)


def app():
    tasks = load_tasks()
    load_nodes(tasks)
    sync_queue(tasks)

    while True:
        print("""
========== TO DO LIST ==========

    1. Add Task
    2. Show All Tasks
    3. Search Task
    4. Update Task
    5. Delete Task
    6. Complete Task
    7. Show Completed Tasks
    8. Show Pending Tasks
    9. Show Queue

        10. Exit

================================
""")

        choice = input("Choose: ")

        if choice == "1":
            task_id = int(input("Enter ID: "))
            title = input("Enter title: ")
            description = input("Enter description: ")

            if add_node(task_id, title, description):
                enqueue(task_id)
                save_data()
                print("Task added successfully!")
            else:
                print("This ID already exists!")

        elif choice == "2":
            show_nodes()

        elif choice == "3":
            task_id = int(input("Enter ID: "))
            task = search_node(task_id)

            if task:
                print(task)
            else:
                print("Task not found!")

        elif choice == "4":
            task_id = int(input("Enter ID: "))
            title = input("New title: ")
            description = input("New description: ")

            if update_node(task_id, title, description):
                save_data()
                print("Task updated!")
            else:
                print("Task not found!")

        elif choice == "5":
            task_id = int(input("Enter ID: "))

            if delete_node(task_id):
                remove_task(task_id)
                save_data()
                print("Task deleted!")
            else:
                print("Task not found!")

        elif choice == "6":
            task_id = int(input("Enter ID: "))

            if complete_node(task_id):
                remove_task(task_id)
                save_data()
                print("Task completed!")
            else:
                print("Task not found!")

        elif choice == "7":
            show_completed()

        elif choice == "8":
            show_pending()

        elif choice == "9":
            show_queue()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")
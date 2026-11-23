from linked import*
from tasks import*
from queue import dequeue,enqueue
from stack import*

def showMenu():
    print("""
    ========== TODO MENEGER ========== 
        1. Add task
        2. Update task
        3. Remove task
        4. Show all tasks
        5. Add task to queue
        6. Complete next task
        7. Undo
        8. Task history
        9. Show queue

           0. Exit
    """)
def app():

    while True:
        showMenu()

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")

            addTask(name)

            if tasks:
                push(tasks[-1])

        elif choice == "2":
            showTasks()

            try:
                taskID = int(input("Enter task ID: "))
                taskName = input("Enter new task name: ")

                updateTask(taskID, taskName)

            except ValueError:
                print("Invalid ID!")

        elif choice == "3":
            showTasks()

            try:
                taskID = int(input("Enter task ID: "))
                removeTask(taskID)

            except ValueError:
                print("Invalid ID!")

        elif choice == "4":
            showTasks()

        elif choice == "5":
            showTasks()

            try:
                taskID = int(input("Enter task ID: "))
                task = findTask(taskID)

                if task:
                    if task["status"] == "Pending":
                        enqueue(task)
                        print("Task added to queue!")
                    else:
                        print("Task is already completed!")
                else:
                    print("Task not found!")


            except ValueError:
                print("Invalid ID!")

        elif choice == "6":
            task = dequeue()

            if task is not None:
                task["status"] = "Completed"
                print(f"{task['name']} completed successfully!")

        elif choice == "7":
            undo(tasks)

        elif choice == "8":
            if not stack:
                print("Task history is empty!")
            else:
                print("\nTask History:")

                for task in stack:
                    print(task)

        elif choice == "9":
            print("\nTask Queue:")
            display()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
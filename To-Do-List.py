tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

def show_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

def clear_tasks():
    tasks.clear()
    print("All tasks cleared.")

while True:
    print("\n====== To-Do List ======")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        clear_tasks()
    elif choice == '5':
        print("Exiting the To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

my_tasks = []

def add_task(task):
    my_tasks.append(task)

def view_tasks():
    if len(my_tasks) == 0:
        print("No tasks yet!")
    else:
        for i, task in enumerate(my_tasks):
            print(f"{i+1}. {task}")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            print("Task added!")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
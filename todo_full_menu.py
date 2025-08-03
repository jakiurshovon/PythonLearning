import os

# Load saved tasks
todo_list = []
if os.path.exists("todo.txt"):
    with open("todo.txt", "r") as file:
        for line in file:
            if "|" in line:
                task_text, done_status = line.strip().split("|")
                todo_list.append({
                    "task": task_text,
                    "done": done_status == "1"
                })

def show_menu():
    print("\n====== TO DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Exit")

def add_task():
    task = input("Enter new task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\n--- Your TO DO List ---")
        for i, item in enumerate(todo_list, start=1):
            status = "✅" if item["done"] else "❌"
            print(f"{i}. {item['task']} [{status}]")

def mark_done():
    view_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    with open("todo.txt", "w") as file:
        for item in todo_list:
            done = "1" if item["done"] else "0"
            file.write(f"{item['task']}|{done}\n")
    print("Tasks saved to todo.txt")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

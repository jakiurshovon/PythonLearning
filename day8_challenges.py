import os

todo_list = []

# Load tasks from file if exists
if os.path.exists("todo.txt"):
    with open("todo.txt", "r") as file:
        for line in file:
            if "|" in line:
                task_text, done_status = line.strip().split("|")
                task_dict = {
                    "task" : task_text,
                    "done" : done_status == "1"  # convert string to boolean
                }
                todo_list.append(task_dict)


while True:
    print((".........To Do List........."))
    print("1. Add tasks")
    print("2. View all tasks")
    print("3. Mark tasks as done")
    print("4. Delete a task")
    print("5. Save the task")
    print("6. Exit")

    choice = input("Chose an option (1-6): ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append({"task" : task, "done" : False})
        print("Task Added Successfully")
    
    elif choice == "2":
        if not todo_list:
            print("Your To Do list is Empty!")
        else:
            print("\n---Your TO DO List---")
        
            for i, item in enumerate(todo_list, start = 1):
                status = "✅" if item["done"] else "❌"
                print(f"{i}. {item['task']} [{status}]")
    
    elif choice == "3":
        task_num = int(input("Enter task number to mark as done: "))

        if 1 <= task_num <= len(todo_list):
            todo_list[task_num-1]["done"] = True
            print("Task marked Done")
        else:
            print("Invalid Task number")
    
    elif choice == "4":
        if not todo_list:
            print("The task list is empty")
        else:
            print("\n---Your TO DO List---")
            del_task = int(input("Enter task number to delete the task: "))

            if 1 <= del_task <= len(todo_list):
                todo_list[del_task-1]["done"] = True
                print("Task marked Done")
            else:
                print("Invalid Task number")
    
    elif choice == "5":
        with open("todo.txt", "w") as file:
            for item in todo_list:
                task = item["task"]
                done = 1 if item["done"] else "0"
                file.write(f"{task}|{done}\n")
                print("Tasks saved to todo.txt")

    
    elif choice == "6":
        print("Goodby")
        break
    else:
        print("Invalid Choice")
            


        
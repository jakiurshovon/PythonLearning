todo_list = []
while True:
    print((".........To Do List........."))
    print("1. Add tasks")
    print("2. View all tasks")
    print("3. Mark tasks as done")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Chose an option (1-4): ")

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
        print("Goodby")
        break
    else:
        print("Invalid Choice")
            


        
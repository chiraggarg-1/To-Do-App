def task():
    tasks = []
    print(input("---Welcome To Task Management App---"))
    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's task are \n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter task you want to update = ")
            if updated_val in tasks:
                up = input("Enter the new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"updated task {up}")




        elif operation == 3:
            deleted_val = input("Enter the task you want to delete = ")
            if deleted_val in tasks:
                delete = tasks.index(deleted_val)
                del tasks[delete]
                print(f"Task {deleted_val} has been deleted...")



        elif operation == 4:
            print(f"Total task = {tasks}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("INVALID INPUT")

task()
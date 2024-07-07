tasks = []

if __name__ == "__main__":

    while True:
        choice = int(
            input(
                "Enter 1 to add a task\n2 to see all tasks\n3 too delete tasks\n0 to exit\nEntered Num:"
            )
        )
        if choice == 0:
            break
        elif choice == 1:
            todo = input("enter your task ")
            tasks.append(todo)
            if todo:
                print("task added ")
                print("-----------------------")
        elif choice == 2:
            print("Here is you're all tasks")
            print("-----------------------")
            for index, task in enumerate(tasks):
                print(f"{index + 1}: {task}")
            print("-----------------------")
        elif choice == 3:
            print("Here  is your all tasks")
            print("-----------------------")
            for index, task in enumerate(tasks):
                print(f"{index + 1}: {task}")
                print("-----------------------")
            try:
                task_num = int(
                    input("Select the number of task for deletion operation perform ")
                )
                if 0 < task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(
                        f"you're task:- [ {removed_task} ] is deleted, enter 2 to see all you're tasks "
                    )
                else:
                    print("Number is greater then task length or smaller ")

            except:
                print("Invalid input. Please enter a valid task number.")
        else:
            print("Invalid choice Enter Only Numbers")
print("Thanks have a great day!!")

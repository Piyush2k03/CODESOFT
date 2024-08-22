def main():
    tasks = []

    while True:
        print("\n------ To-Do List------")
        print("1.Add Your Task")
        print("2. Show Added Tasks")
        print("3. Mark Task as Done")
        print("4. Exit from To-Do List")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Your choice is Invalid. Please try again.")

if __name__ == "__main__":
    main()
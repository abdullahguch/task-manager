# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_path = "tasks.txt"  # File to store tasks

        # Load tasks from the file
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    task, completed = line.strip().split(",")
                    self.tasks.append({"task": task, "completed": completed.lower() == "true"})
        except FileNotFoundError:
            # If the file is not found, it's okay, just start with an empty task list
            pass

    def save_tasks(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(f"{task['task']},{task['completed']}\n")

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        try:
            index = int(task_index) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["completed"] = True
                self.save_tasks()
                print(f"Task '{self.tasks[index]['task']}' marked as completed!")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid task index.")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_index = input("Enter the task index to mark as completed: ")
            task_manager.mark_completed(task_index)
        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

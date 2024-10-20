import os

# Task Manager Class
class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    # Load tasks from file
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    task_name, status = line.strip().split(",")
                    self.tasks.append({"task": task_name, "status": status == "True"})
        else:
            open(self.filename, "w").close()  # Create the file if it doesn't exist

    # Save tasks to file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f'{task["task"]},{task["status"]}\n')

    # Display the task list
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nCurrent Task List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Complete" if task["status"] else "Incomplete"
                print(f"{i}. {task['task']} - {status}")

    # Add a new task
    def add_task(self):
        task_name = input("Enter the task description: ")
        self.tasks.append({"task": task_name, "status": False})
        self.save_tasks()
        print(f"Task '{task_name}' added!")

    # Edit an existing task
    def edit_task(self):
        self.display_tasks()
        try:
            task_num = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_num < len(self.tasks):
                new_task_name = input("Enter the new task description: ")
                self.tasks[task_num]["task"] = new_task_name
                self.save_tasks()
                print("Task updated!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    # Delete a task
    def delete_task(self):
        self.display_tasks()
        try:
            task_num = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_num < len(self.tasks):
                removed_task = self.tasks.pop(task_num)
                self.save_tasks()
                print(f"Task '{removed_task['task']}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    # Mark a task as complete
    def mark_task_complete(self):
        self.display_tasks()
        try:
            task_num = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_num < len(self.tasks):
                self.tasks[task_num]["status"] = True
                self.save_tasks()
                print(f"Task '{self.tasks[task_num]['task']}' marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    # Menu for user interaction
    def show_menu(self):
        while True:
            print("\nTask Manager")
            print("1. View tasks")
            print("2. Add task")
            print("3. Edit task")
            print("4. Delete task")
            print("5. Mark task as complete")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                self.display_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.edit_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

# Main execution
if __name__ == "__main__":
    manager = TaskManager()
    manager.show_menu()

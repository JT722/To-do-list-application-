import json
import os

# Load tasks from file
def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx}. {task['description']} [Status: {status}]")

# Add a new task
def add_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        print(f"Task '{description}' added!")
    else:
        print("Task description cannot be empty!")

# Edit an existing task
def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to edit: "))
        if 1 <= task_number <= len(tasks):
            new_description = input("Enter the new description: ").strip()
            if new_description:
                tasks[task_number - 1]["description"] = new_description
                print("Task updated!")
            else:
                print("Task description cannot be empty!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['description']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Mark a task as complete
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the task manager
def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Mark task as complete")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

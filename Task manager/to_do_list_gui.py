import json
import os
import tkinter as tk
from tkinter import messagebox

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

# Refresh the listbox
def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        task_listbox.insert(tk.END, f"{idx+1}. {task['description']} [Status: {status}]")

# Add task
def add_task():
    description = task_entry.get()
    if description:
        tasks.append({"description": description, "completed": False})
        task_entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty.")

# Mark task as complete
def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks[task_index]['completed'] = True
        refresh_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

# Delete task
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        del tasks[task_index]
        refresh_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create the GUI
root = tk.Tk()
root.title("Task Manager")

# Entry for new task
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Mark Complete and Delete buttons
complete_button = tk.Button(root, text="Mark Complete", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Load tasks and refresh display
tasks = load_tasks()
refresh_tasks()

# Save tasks when window is closed
def on_closing():
    save_tasks(tasks)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import json


tasks = []


def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        save_tasks()
        list_update()
        task_field.delete(0, 'end')


def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task = task_listbox.get(task_index)
        confirmation = messagebox.askyesno('Confirmation', f"Are you sure you want to delete '{task}'?")
        if confirmation:
            tasks.remove(task)
            save_tasks()
            list_update()


def delete_all_tasks():
    confirmation = messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?')
    if confirmation:
        tasks.clear()
        save_tasks()
        list_update()


def list_update():
    task_listbox.delete(0, "end")
    sorted_tasks = sorted(tasks)
    for task in sorted_tasks:
        task_listbox.insert("end", task)


def close():
    save_tasks()
    guiWindow.destroy()


def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks.extend(json.load(file))
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("500x450")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#E0F0F0")

    load_tasks()

    header_frame = tk.Frame(guiWindow, bg="#E0F0F0")
    functions_frame = tk.Frame(guiWindow, bg="#E0F0F0")
    listbox_frame = tk.Frame(guiWindow, bg="#E0F0F0")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both", padx=10)
    listbox_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Segoe UI", 30),
        background="#E0F0F0",
        foreground="#333333"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Segoe UI", 11, "bold"),
        background="#E0F0F0",
        foreground="#333333"
    )
    task_label.pack(pady=10)

    task_field = ttk.Entry(
        functions_frame,
        font=("Segoe UI", 12),
        width=18,
        background="#FFFFFF",
        foreground="#333333"
    )
    task_field.pack(pady=5)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task,
        style="Custom.TButton"
    )
    add_button.pack(pady=5)

    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task,
        style="Custom.TButton"
    )
    del_button.pack(pady=5)

    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks,
        style="Custom.TButton"
    )
    del_all_button.pack(pady=5)

    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close,
        style="Custom.TButton"
    )
    exit_button.pack(pady=5)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#333333",
        selectbackground="#CCCCCC",
        selectforeground="#333333",
        bd=0,
        relief=tk.SOLID,
        highlightthickness=0,
        activestyle='none'
    )
    task_listbox.pack(fill="both", expand=True)

    list_update()

    style = ttk.Style()
    style.configure("Custom.TButton",
                    font=("Segoe UI", 10),
                    background="#CCCCCC",
                    foreground="#333333",
                    relief=tk.SOLID,
                    borderwidth=0,
                    highlightthickness=0,
                    padx=5,
                    pady=2,
                    anchor="center"
                    )

    guiWindow.mainloop()

import json


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.save_tasks()

    def delete_all_tasks(self):
        self.tasks.clear()
        self.save_tasks()

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks.extend(json.load(file))
        except FileNotFoundError:
            pass


import unittest


class ToDoListTests(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        task = "Test Task"
        self.todo_list.add_task(task)
        self.assertIn(task, self.todo_list.tasks)

    def test_delete_task(self):
        task = "Test Task"
        self.todo_list.tasks.append(task)
        self.todo_list.delete_task(task)
        self.assertNotIn(task, self.todo_list.tasks)

    def test_delete_all_tasks(self):
        self.todo_list.tasks.extend(["Task 1", "Task 2", "Task 3"])
        self.todo_list.delete_all_tasks()
        self.assertEqual(len(self.todo_list.tasks), 0)


if __name__ == '__main__':
    unittest.main()

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

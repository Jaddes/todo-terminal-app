# from typing import List
# import json

# class ToDoList:
#     """Manages a collection of tasks."""

#     def __init__(self):
#         """Initialize an empty to-do list."""
#         self.tasks: List[Task] = []

#     def add_task(self, title: str) -> None:
#         """Add a new task with the given title."""
#         self.tasks.append(Task(title))

#     def list_tasks(self) -> None:
#         """Print all tasks with their status."""
#         if not self.tasks:
#             print("No tasks found.")
#             return

#         for idx, task in enumerate(self.tasks, start=1):
#             status = "✔️" if task.completed else "❌"
#             print(f"{idx}. [{status}] {task.title}")

#     def mark_task_completed(self, task_id: int) -> None:
#         """Mark the task with the given ID as completed."""
#         if 1 <= task_id <= len(self.tasks):
#             self.tasks[task_id - 1].completed = True
#         else:
#             print("Invalid task ID.")

#     def delete_task(self, task_id: int) -> None:
#         """Delete the task with the given ID."""
#         if 1 <= task_id <= len(self.tasks):
#             del self.tasks[task_id - 1]
#         else:
#             print("Invalid task ID.")

#     def save_to_file(self, filename: str) -> None:
#         """Save tasks to a file in JSON format."""
#         data = [{"title": task.title, "completed": task.completed} for task in self.tasks]
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)

#     def load_from_file(self, filename: str) -> None:
#         """Load tasks from a file."""
#         try:
#             with open(filename, 'r') as f:
#                 data = json.load(f)
#                 self.tasks = [Task(item["title"]) for item in data]
#                 for task, item in zip(self.tasks, data):
#                     task.completed = item.get("completed", False)
#         except FileNotFoundError:
#             print(f"File '{filename}' not found. Starting with an empty to-do list.")

# todo.py - Simple terminal To-Do list application
# This project demonstrates the applications of Python fundamentals such as:
#   - Object-Oriented Programming (OOP)
#   - File input/output (saving and loading tasks)
#   - Basic CRUD operations (Create, Read, Update, Delete)
#
# Project description:
#   - Summarize the information learned in the Python course (Learn Python 3 - Code)
#   - As proof of understanding of basic Python programming skills
#

# Complexity: Easy
# Technologies: Python 3

# One task for each task in to-do list
class Task:
    """
    Represents one task in the to-do list

    Attributes:
        title (str): The title or description of the task.
        completed (bool): Task completion status.
    """
    def __init__(self, title):
        """
        Initialize a new Task instance.
        
        Attributes:
            title (str): Task title or task description.
        
        Example:
            task = Task("Finish the project")
        """
        self.title = title
        self.completed = False

    def mark_completed(self):
        """"
        Mark the task completed.
        
        Example:
            task.mark_completed()
        """
        self.completed = True
def __str__(self):
        """
        Return a string representation of the task.
        Shows [X] if completed, [ ] if not.
        
        Example:
            print(task)
        """
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.title}"

# -----------------------
# ToDoList class
# Stores list of Task objects
# Methods:
# - add_task(title)
# - list_tasks()
# - mark_task_completed(task_id)
# - delete_task(task_id)
# - save_to_file(filename)
# - load_from_file(filename)
# -----------------------

# -----------------------
# CLI Menu
# Display choices to the user:
# 1. Add a task
# 2. List all tasks
# 3. Mark a task as completed
# 4. Delete a task
# 5. Save and exit
# -----------------------

# -----------------------
# Main function
# Application entry point
# Loads tasks from file
# Runs CLI loop
# Saves tasks on exit
# -----------------------
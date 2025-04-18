# todo.py

# -----------------------
# Task class
# Represents a single to-do item
# Attributes: title, completed (bool)
# Methods: mark as completed
# -----------------------
class Task:
    """
    Represents a single task in the to-do list
    """
    
    def __init__(self, title):
        """
        Initialize a new task with a title.
        By default task is not completed.
        """
        self.title = title
        self.completed = False
    
    def mark_completed(self):
        """
        Mark the task completed.
        """
        self.completed = True
        
    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.title}"

# -----------------------
# ToDoList class
# Manages a list of Task objects
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
# Display options to the user:
# 1. Add a task
# 2. List all tasks
# 3. Mark a task as completed
# 4. Delete a task
# 5. Save and Exit
# -----------------------

# -----------------------
# Main function
# Entry point of the application
# Loads tasks from file
# Runs the CLI loop
# Saves tasks on exit
# -----------------------
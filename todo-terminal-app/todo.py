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

from typing import List
import json

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


class ToDoList:
    """
    Represents a collection of tasks managed by ToDoList.
    
    Attributes:
        title (List[Task]): A list holdin Task objects.
    """
    
    def __init__(self):
        """Initialization of an empty to-do list."""
        self.tasks: List[Task] = []
            # We could write it like 'self.tasks = []'
            # Like this now any new user viewing this code knows that this list is labeled for "Tasks" 

    def add_task(self, title: str) -> None:
        """ 
        Add a new task with the given title. 
        
        Args:
            title (str): The title or description of the task.

        Example:
            new_todolist = ToDoList()
            new_todolist.add_task("Finish the project")
        """
        self.tasks.append(Task(title))
        # We could have written it like:
        #   def add_task(self, title):
        #       self.tasks.append(Task(title))
        # But adding "title: str" and "-> None" makes it more easier to understand and test by the new users

    def list_tasks(self) -> None:
        """
        Print all tasks with their status.
        
        Example:
            new_todolist = ToDoList()
            new_todolist.list_tasks()
        """
        
        if not self.tasks:
        # Check if the list is empty
            print("No tasks found.") 
            return
        
        for idx, task in enumerate(self.tasks, start=1):
            # enumerate counts and go trough the giving list making counting a lot easier
            # so there is the idx which is just declared
            # enumerate just affects the print not the list
            status = "✅" if task.completed else "❌"
            print(f"{idx}. [{status} {task.title}]")
            
    def mark_task_completed(self, task_id: int) -> None:
        """
        Mark the task with the given ID as completed.
        
        Agrs:
            task_id(int): The given id that is to be marked as finshed
            
        Example:
            new_todolist = ToDoList()
            new_todolist.mark_task_completed(2)
        """
        if 1 <= task_id <= len(self.tasks):
            self.tasks[task_id - 1].completed = True
        else:
            print("Invalid task ID")
            
    def delete_task(self, task_id: int) -> None:
        """
        Delete the task with the given ID.
        
        Args:
            task_id(int): The given id that is marked for delete
            
        Example:
            new_todolist = ToDoList()
            new_todolist.delete_task(2)
        """ 
        if 1 <= task_id <= len(self.tasks):
            del self.tasks[task_id - 1]
        else:
            print("Invalid task ID")
    
    def save_to_file(self, filename: str) -> None:
        """
        Save tasks to a file in JSON format

        Args:
            filename (str): name of a file where we want to save the file
            
        Example:
            new_todolist = ToDoList()
            new_todolist.save_to_file("Project.json") 
        """
        data = [{"title": task.title, "completed": task.completed} for task in self.tasks]
        # list comprehension is more easier to make then using basic for + append or even map()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            # indent used for dictonary to be pretty
            
    def load_from_file(self, filename: str) -> None:
        """
        Load tasks from a file
        
        Args:
            filename(str): name of a file where we want to load from
            
        Example:
            new_todolist = ToDoList()
            new_todolist.load_from_file("Project.json") 
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task(item["title"]) for item in data]
                # make list based on first word inside the dictionary
                for task, item in zip(self.tasks, data):
                    task.completed = item.get("completed", False)
                    # default version supposed to set on False and if not empty he just gonna write what in the dictionary                    
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty to-do list.")
        
            


def main():
    todo_list = ToDoList()
    filename = "tasks.json"

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save and Exit")
        print("6. Load tasks from a file")  


        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the task title: ")
            todo_list.add_task(title)

        elif choice == "2":
            todo_list.list_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter the task number to mark as completed: "))
                todo_list.mark_task_completed(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            todo_list.save_to_file(filename)
            print("Tasks saved successfully! Goodbye 👋")
            break
        
        elif choice == "6":
            filename = input("Enter the filename to load tasks from: ")
            todo_list.load_from_file(filename)
            print(f"Tasks loaded from '{filename}' successfully!")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            

if __name__ == "__main__":
    main()
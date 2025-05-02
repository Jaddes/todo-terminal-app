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
import os

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
        title (List[Task]): A list holding Task objects.
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
        # We could have written it like:
        #   def add_task(self, title):
        #       self.tasks.append(Task(title))
        # But adding "title: str" and "-> None" makes it more easier to understand and test by the new users
        self.tasks.append(Task(title))
    
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
        
        Args:
            task_id(int): The given id that is to be marked as finished
            
        Example:
            new_todolist = ToDoList()
            new_todolist.mark_task_completed(2)
        """
        if 1 <= task_id <= len(self.tasks):
            self.tasks[task_id - 1].completed = True
            # Example easier to understand:
            # We want task 1. In listed function with enumerate its in the position 1. We write 1 and the position [0] where its our first to-do task
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
        # List comprehension is more easier to make then using basic for + append or even map()
        # So we make here a dictionary from the tasks we are implementing 
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            # indent used for dictionary to make enough space to see clearly and to be more organized for human eye
            
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
                # Make list based on first word inside the dictionary 
                # We are implementing just the value from 'title'
                for task, item in zip(self.tasks, data):
                    task.completed = item.get("completed", False)
                    # We need to add the second part which is completed value so that's why we are using for loop
                    # Default version supposed to set on False and if not empty he just gonna write what in the dictionary                    
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty to-do list.")
            
    def merge_and_save_to_file(self, filename: str) -> None:
        """
        Merge existing tasks in the to-do list with current tasks and save it all together.

        Args:
            filename (str): The to-do list to save the merged tasks into.
        """
        try:
            with open(filename, "r") as f:
                old_data = json.load(f)
        except FileNotFoundError:
            old_data = []
        # First we are making dictionary from the loaded json file
            
        old_tasks = [Task(item["title"]) for item in old_data]
        # Like from the previous command now we are making the list just from the title parts
        for task, item in zip(old_tasks, old_data):
            task.completed = item.get("completed", False)
            
        # Merge old tasks with new ones
        merged_tasks = old_tasks + self.tasks
        
        # Prepare data for saving
        data = [{"title": task.title, "completed": task.completed} for task in merged_tasks]
        
        # Save merged tasks back to file
        with open(filename, "w") as f:
            json.dump(data, f, indent = 4)
        
def choose_file():
    """
    Shows the list of all available to-do lists.

    """
    folder = "projects"
    files = [f for f in os.listdir(folder) if f.endswith(".json")]
    # We choose and open the folder premade projects and only made a list made of .json files
    
    if not files:
        print("No to-do list files found.")
        return None
    
    print("\nAvailable To-Do Lists:")
    for idx, filename in enumerate(files, start=1):
        print(f"{idx}. {filename}")
        
    try:
        choice = int(input("Choose a file by number: "))
        if 1 <= choice <= len(files):
            return os.path.join(folder, files[choice - 1])
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None     
    
   


def main():
    todo_list = ToDoList()
    filename = None

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save and Exit")
        print("6. Load tasks from a file")  


        choice = input("Enter your choice (1-6): ")

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
            if filename is None:
                print("You're to-do tasks are not saved on any to-do list what do you want to do?\n")
                
                print("\nSave Options:")
                print("1. Save to an existing to-do list")
                print("2. Save as a new to-do list")
                
                save_choice = input("Enter your choice (1-2): ")
                
                if save_choice == "1":
                    # Let user choose an existing file
                    selected_file = choose_file()
                    if selected_file:
                        todo_list.merge_and_save_to_file(selected_file)
                        filename = selected_file  # Update filename after saving
                        print(f"Tasks saved to '{selected_file}' successfully! A Goodbye 👋")
                        break
                    else:
                        print("No file selected. Returning to menu.")
                        
                    
                elif save_choice == "2":
                    new_name = input("Enter new project name (without .json) ").strip()
                    if not new_name.endswith(".json"):
                        new_name += ".json"
                    new_path = os.path.join("projects", new_name)
                    todo_list.save_to_file(new_path)
                    print(f"Tasks saved as new project '{new_path}' successfully! Goodbye 👋")
                    break
            else:
                # filename is already set by 6 choice
                todo_list.save_to_file(filename)
                print(f"Tasks saved to '{filename}' successfully! Goodbye 👋")
                break
            
        
        elif choice == "6":
            selected_file = choose_file()
            if selected_file:
                todo_list.load_from_file(selected_file)
                print(f"Tasks loaded from '{selected_file}' successfully!")
                filename = selected_file
            else:
                print("No file selected. Returning to menu.")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            

if __name__ == "__main__":
    main()
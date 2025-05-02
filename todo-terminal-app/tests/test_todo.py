import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from todo import ToDoList, Task
import unittest
import json

class TestToDoList(unittest.TestCase):
    def setUp(self):
        """
        Prepare a fresh enviroment before each test function runs.
        
        - This method automatically runs ,before every single test method, inside the test class.
        - When Python executes a test, it first calls 'setUp()'. then runs the actual test function.
        
        Why do we use it?
        -----------------
        We want every test to start with a fresh, clean, and isolated state.
        Without this, changes made in one test could affect the next test, causing unreliable results.
        
        What it does here:
        - `self.todo = ToDoList()` creates a new, empty To-Do list object before each test.
        - `self.test_file = "test_task.json"` sets up a filename used for temporary file tests, 
        ensuring we do not affect real project files during testing.
        
        This ensures all test are indepedent, repeatable, and safe for testing.
        """
        self.todo = ToDoList()              # Step 1: Create an empty To-Do list before each test
        self.test_file = "test_task.json"   # Step 2: Set up a temporary test file name
        
    def tearDown(self):
        """
        Clean up after each test function runs.
        
        - This method automatically runs after every single test method inside the test class.
        - When Python finishes running a test, it immediatly calls tearDown() to perform cleanup.
        
        Why do we use it?
        -----------------
        We want to ensure that temporary files or resources created during testing are removed.
        Without cleanup, leftover files could:
            - Interfere with other test.
            - Cause disk clutter.
            - Lead to false positives or negatives in testing results.
            
        What it does here:
        ------------------
        - Checks if the remporary test file (`self.test_file`) exists.
        - If it does, deletes it using `os.remove()`.
        
        This guarantees that each test leaves **no side effects**, keeping the testing environment **clean and isolated**.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_task(self):
        """
        Test the functionality of adding a task to the ToDoList.
        
        Purpose:
        --------
        Verify that when a new task is added:
            - It correctly increases the number of tasks in the list.
            - The added task has the correct title.
            - The added task is initially marked as not completed.
            
        Steps performed:
        ----------------
        1. Add a task with the title "Test Task" to the ToDoList.
        2. Assert that the number of tasks (`len(self.todo.tasks)`) is exactly 1.
        3. Assert that the title of the first task is "Test Task".
        4. Assert that the 'completed' status of the task is False (i.e., not completed yet).
        
        This test ensures that the 'add_task()' method behaves correctly and that new tasks 
        are properly initialized with correct default values. 
        """
        name = "Test Task"
        self.todo.add_task(name) # Step 1: Add a task with a specific title
        self.assertEqual(len(self.todo.tasks), 1) # Step 2: Check that exactly one task is now in the list
        self.assertEqual(self.todo.tasks[0].title, name) # Step 3: Check that the task title matches
        self.assertFalse(self.todo.tasks[0].completed) # Step 4: Verify that task is not completed by default
        
    def test_delete_task(self):
        """
        Test the functionality of deleteing a task fro mthe ToDoList.
        
        Purpose:
        --------
        Verify that when a task is deleted:
            - The task is correctly removed from the list.
            - The total number of tasks decreases accordingly.
        
        Steps performed:
        ----------------
        1. Add a task with the title "Task to delete" to the ToDoList.
        2. Delete the task at index 1 using the 'delete_task' method.
        3. Assert that the task list is now empty (lenght = 0).
        
        This test ensure that 'delete_task()' method removes tasks correctly 
        and maintains the integrity of the tasks list.
        """
        self.todo.add_task("Task to delete") # Step 1: Adda task to the list
        self.todo.delete_task(1)             # Step 2: Delete the task at position 1
        self.assertEqual(len(self.todo.tasks), 0)   # Step 3: Verify that the list is now empty
        
    def test_mark_task_completed(self):
        """
        Test the functionality of marking a task as completed in the ToDoList.
        
        Purpose:
        --------
        Verify that when a task is marked as completed:
            - The 'completed' attribute of the correct task is set ot True.
            
        Steps performed:
        ----------------
        1. Add a task with the title "Task to complete" to the ToDoList.
        2. Mark the task at index 1 as completed using 'mark_task_completed' method.
        3. Assert that the 'completed' status of the task is now True.
        
        This test ensures that the 'mark_task_completed()' method is properly updating the completion status of the task.
        """
        self.todo.add_task("Task to complete") # Step 1: Add a new task
        self.todo.mark_task_completed(1) # Step 2: Mark the first task as completed
        self.assertTrue(self.todo.tasks[0].completed) # Step 3: Verify that the task is now marked 
        
    def test_save_to_file(self):
        """
        Test the functionality of saving tasks to a file in JSON format.
        
        Purpose:
        --------
        Verify that when tasks are save:
            - A file is successfully created.
            - The file contains the correct task data (title and completion status).
            
        Steps performed:
        ----------------
        1. Add a task with the title "Task to save" to the ToDoList.
        2. Save the ToDoList to a test JSON file using 'save_to_file'.
        3. Assert that the test file now exists on the filesystem.
        4. Open the file and load its contents as JSON
        5. Assert that:
            - The title of the first task matches "Task to save".
            - The 'completed' status of the first task is False.
            
        This test ensures that the 'save_to_file()' method correctly writes the tasks to disk 
        int the expected format.
        """
        self.todo.add_task("Task to save")    # Step 1: Add a task
        self.todo.save_to_file(self.test_file)  # Step 2: Save the task list to a file
        self.assertTrue(os.path.exists(self.test_file)) # Step 3: Check that the file was created
        
        with open(self.test_file, "r") as f:    # Step 4: Open the save file
            data = json.load(f)
            self.assertEqual(data[0]["title"], "Task to save")  # Step 5a: Check title
            self.assertFalse(data[0]["completed"])  # Step 5b: Check that it's not completed
            
    def test_load_from_file(self):
        """
        Test the funcionality of loading tasks from a JSON file into the ToDoList.
        
        Purpose:
        --------
        Verify that when a file containing tasks is loaded:
            - The correct number of tasks is added to the ToDoList.
            - Each tasks's attributes (title and comletion status) are properly restored.
            
        Steps performed:
        ----------------
        1. Manually create a JSON file containg one task with a specific title and completed status.
        2. Use the 'load_from_file' method to load tasks from the test file into the ToDoList.
        3. Assert that :
            - Exactly one task was loaded.
            - The loaded task has correct title "Loaded Task".
            - The loaded task's 'completed' atribute is True.
            
        This test ensures that the 'load_from_file()' method correctly reads from 
        disk and reconstructs the tasks into proper Task objects.
        """
        # Step 1: Manually create and save JSON data
        tasks_data = [{"title": "Loaded Task", "completed": True}]
        with open(self.test_file, "w") as f:
            json.dump(tasks_data, f)

        # Step 2: Load the data into a fresh ToDoList
        self.todo.load_from_file(self.test_file)
        
        # Step 3: Assertions to verify correctness
        self.assertEqual(len(self.todo.tasks), 1)       # Check one task was loaded
        self.assertEqual(self.todo.tasks[0].title, "Loaded Task")   # Check the task title
        self.assertTrue(self.todo.tasks[0].completed)   # CHeck the task completion status

    def test_merge_and_save_to_file(self):
        """
        Test the functionality of merging new tasks with existing tasks and saving them to a file.

        Purpose:
        --------
        Verify that when merging:
        - Existing tasks in the file are preserved.
        - New tasks added during the current session are appended.
        - The final saved file contains both old and new tasks in the correct order.

        Steps performed:
        ----------------
        1. Manually create and save a JSON file with one existing task.
        2. Add a new task using the ToDoList object.
        3. Merge and save the new task into the same file using `merge_and_save_to_file`.
        4. Open the file and load its contents.
        5. Assert that:
        - The total number of tasks is now 2.
        - The first task matches the existing task.
        - The second task matches the newly added task.

        This test ensures that the `merge_and_save_to_file()` method correctly combines previous saved data
        with new in-memory tasks without overwriting existing information.
        """
        # Step 1: Create a file with an existing task
        existing_tasks = [{"title": "Old Task", "completed": False}]
        with open(self.test_file, "w") as f:
            json.dump(existing_tasks, f)

        # Step 2: Add a new task into ToDoList
        self.todo.add_task("New Task")
        
        # Step 3: Merge and save the new task into the same file
        self.todo.merge_and_save_to_file(self.test_file)

        # Step 4: Read the merged file and validate its contents
        with open(self.test_file, "r") as f:
            merged_tasks = json.load(f)
            self.assertEqual(len(merged_tasks), 2)  # Two tasks should now exist
            self.assertEqual(merged_tasks[0]["title"], "Old Task")  # First task is the old one
            self.assertEqual(merged_tasks[1]["title"], "New Task")  # Second task is the new one

if __name__ == "__main__":
    unittest.main()
        
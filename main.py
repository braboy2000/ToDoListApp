"""
To-Do List CLI Commands

    Add a Task (1)

        Prompts the user to enter a new task.

        Saves the task to a list and writes it to a file.

    View Tasks (2)

        Reads the list of tasks from the file.

        Displays them with numbers for easy reference.

    Mark a Task as Completed (3)

        Asks for a task number.

        Marks the selected task as completed (e.g., by adding "[✔]" to it).

        Updates the file.

    Remove a Task (4)

        Asks for a task number.

        Deletes the selected task from the list.

        Updates the file.

    Exit the Program (5)

        Closes the app.

        Ensures that tasks are saved before exiting.
"""


def add_task(task):
    with open('tasks.txt',"a") as taskfile:
        taskfile.write(task)

def view_tasks():
     with open('tasks.txt','r') as taskfile:
        tasks=taskfile.readlines()
        for index, task in enumerate(tasks, start=1):
            print(f"{index}.{task.strip()}")


def complete_task():
    with open('tasks.txt','r') as taskfile:
        pass

def remove_task():
    with open('tasks.txt','r') as taskfile:
        pass


menu_options = [
    '1. Add task',
    '2. View tasks',
    '3. Complete task',
    '4. Remove task',
    '5. Exit'
]


choice=''
for option in menu_options:
        print(option)
while choice != str('5'):
    
    choice=input('Please choose an option: ')
    if choice == str('1'):
        task=input('Task to add: ')
        for option in menu_options:
            print(option)
        add_task(task)
    if choice =='2':
        view_tasks()    
    if choice==3:
        pass
    if choice==4:
            pass
            
        
   
    


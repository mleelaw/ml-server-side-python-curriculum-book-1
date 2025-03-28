# initialize an empty to do list
todo_list = []


# function to add a task
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")


# function to remove a task
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")


# function to display all tasks
def display_tasks():
    print("To-Do List:")
    for task in todo_list:
        print(f" - {task}")


# adding tasks
add_task("Read a book")
add_task("Write some code")
add_task("Go for a walk")

# displaying tasks
display_tasks()

# removing a task
remove_task("Write some code")

# displaying tasks again
display_tasks()

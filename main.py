import functions
from time import strftime as st

date_time = st("%b %d, %Y %H:%M:%S")
print(f"It is now {date_time}")

tasks = functions.read_tasks()

while True:
    action = input(f'Type "add", "show", "edit, "complete" or "exit" to quit the program: ').strip()

    if action.startswith("add"):
        task = action.strip("add ") + '\n'

        tasks.append(task)

        functions.create_tasks(tasks)

    elif action.startswith("show"):
        if len(tasks) < 1:
            print(f'You currently have no tasks.')
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1} - {task.title()}", end = "")

    elif action.startswith("edit"):
        try:
            print(f'Use the Numkeys to select the task you would like to edit.')
            i = 1
            for task in tasks:
                print(f'{i}. {task.title()}', end = "")
                i += 1
            task_index = int(input()) - 1
            tasks[task_index] = input(f'Input the new task: ') + '\n'
            
            functions.create_tasks(tasks)
        except ValueError:
            print("Command not recognised.")
            continue

    elif action.startswith("complete"):
        for index, task in enumerate(tasks):
                print(f"{index + 1} - {task.title()}", end = "")
        index = tasks.pop(int(input("Enter the number of the task you completed? ")) - 1)
        
        functions.create_tasks(tasks)

    elif action.startswith("exit"):
        print('Bye!')
        break

    else:
        print(f'Command not recognised')

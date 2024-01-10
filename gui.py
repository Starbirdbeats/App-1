import functions
import PySimpleGUI as sg

layout = [[sg.Text("Create a task:")],
          [sg.InputText(tooltip="Enter a task", key="task"), sg.Button("Add")],
          [sg.Listbox(values=functions.read_tasks(), key="tasks", enable_events=True, size=[45, 10]), sg.Button("Edit")]]

window_main = sg.Window("Simple To-Do App", layout=layout, font=("Montserrat", 8))

while True:
    event, values = window_main.read()
    print(f"{event}\n{values}")
    match event:
        case "Add":
            tasks = functions.read_tasks()
            tasks.append(values["task"])
            functions.create_tasks(tasks)
            window_main["tasks"].update(values=tasks)
        case "Edit":
            task = values["tasks"][0]
            tasks = functions.read_tasks()
            index = tasks.index(task)
            tasks[index] = values["task"]
            functions.create_tasks(tasks)
            window_main["tasks"].update(values=tasks)
        case "tasks":
            window_main["task"].update(value=values["tasks"][0])
        case sg.WIN_CLOSED:
            break
           
 
window_main.close()

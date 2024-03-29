import functions
import PySimpleGUI as sg
from time import strftime

layout = [[sg.Text("", key="clock")],
          [sg.Text("Create a task:")],
          [sg.InputText(tooltip="Enter a task", key="task", size=47), sg.Button("Add")],
          [sg.Listbox(values=functions.read_tasks(), key="tasks", enable_events=True, size=[45, 10]), sg.Button("Edit"), sg.Button("complete")],
          [sg.Button("exit")]]

window_main = sg.Window("Simple To-Do App", layout=layout, font=("Montserrat", 8))

while True:
    event, values = window_main.read(timeout=200)
    window_main["clock"].update(strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            tasks = functions.read_tasks()
            tasks.append(f"{values['task']}\n")
            functions.create_tasks(tasks)
            print(tasks)
            window_main["tasks"].update(values=tasks)
        case "Edit":
            try:
                task = values["tasks"][0]
                tasks = functions.read_tasks()
                index = tasks.index(task)
                tasks[index] = values["task"]
                functions.create_tasks(tasks)
                window_main["tasks"].update(values=tasks)
            except IndexError:
                sg.popup("First select a task, before pressing edit.", font=("Montserrat", 8))
        case "complete":
            try:
                tasks = functions.read_tasks()
                tasks.remove(values["tasks"][0])
                functions.create_tasks(tasks)
                window_main["tasks"].update(values=tasks)
                window_main["task"].update(value="")
            except IndexError:
                sg.popup("First select a task, before pressing complete.", font=("Montserrat", 8))
        case "exit":
            break
        case "tasks":
            window_main["task"].update(value=values["tasks"][0])
        case sg.WIN_CLOSED:
            break
           
 
window_main.close()
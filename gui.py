import functions
import PySimpleGUI as sg

layout = [[sg.Text("Create a task:")],
          [sg.InputText(tooltip="Enter a task", key="task"), sg.Button("Add")]]

window_main = sg.Window("Simple To-Do App", layout=layout, font=("Montserrat", 14))

while True:
    event, values = window_main.read()
    print(f"{event}\n{values}")
    match event:
        case "Add":
            tasks = functions.read_tasks()
            tasks.append(values["task"])
            functions.create_tasks(tasks)
        case sg.WIN_CLOSED:
            window_main.close()

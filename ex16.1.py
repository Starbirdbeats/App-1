import PySimpleGUI as sg

#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter Feet: '), sg.InputText()],
            [sg.Text('Enter Inches:'), sg.InputText()],
            [sg.Button('Convert')]]

# Create the Window
window = sg.Window('Converter', layout)

window.read()
window.close()
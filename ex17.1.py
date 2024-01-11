import PySimpleGUI as sg

def feet_inch_to_meters(feet, inch):
    feet_to_meters = float(feet) * 0.3048
    inch_to_meters = float(inch) * 0.0254
    total_meters = feet_to_meters + inch_to_meters

    return total_meters


layout = [[sg.T("Enter feet: "), sg.InputText(key="feet")],
          [sg.T("Enter inches: "), sg.InputText(key="inches")],
          [sg.Button("Convert"), sg.T("", key="meters")]]

window_main = sg.Window("Converter", layout=layout)

while True:
    event, values = window_main.read()
    print(f"{event}\n{values}")
    match event:
        case "Convert":
            meters = feet_inch_to_meters(values["feet"], values["inches"])
            window_main["meters"].update(f"{meters} m")
        case sg.WIN_CLOSED:
            break

window_main.close()

# if __name__ == "__main__":
#     meters = feet_inch_to_meters(input("Enter feet: "), input("Enter inches: "))
#     print(f"{meters} m")
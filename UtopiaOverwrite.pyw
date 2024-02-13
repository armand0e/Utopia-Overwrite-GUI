import os
from config import Config

try:
    import PySimpleGUI as sg
except:
    os.system("pip install -r requirements.txt")


map_folder = Config.maps_folder_path
    
    
layout = [
    [sg.Frame('Platform:',[[ sg.Radio('Steam', 'radio1', key='-STEAM-', size=(7,1)), sg.Radio('Epic Games', 'radio1', key='-EPIC-',  size=(13,1))]],)],
    [sg.Text('Desired Map:'), sg.Input(key="-IN-"), sg.FileBrowse(initial_folder= map_folder , file_types=( ("UDK", "*.udk"), ("UPK", "*.upk") ))],
    [sg.Button("Overwrite"), sg.Cancel()]
]

window = sg.Window('Utopia Overwrite GUI', layout)

while True:
    event, values = window.read()
   # print(event, '\n', values, '\n')

    if event in (sg.WINDOW_CLOSED, "Cancel"):
        break
    if event == "Overwrite":        
        map = '"' + values["-IN-"] + '"'
        desired_map = ""
        for i in map:
            if i == "/":
                i = "\\"
            desired_map += i
        
        if values["-STEAM-"] == True:
            utopia_path = f"{Config.steam_path}\\rocketleague\\TAGame\\CookedPCConsole\\Labs_Utopia_P.upk"
            os.system("@echo off")
            os.system(f'echo "{desired_map}"')
            os.system(f'echo F|xcopy /y "{desired_map}" "{utopia_path}"')
            sg.popup_auto_close(auto_close_duration=0.2)


        elif values["-EPIC-"] == True:
            utopia_path = f"{Config.epic_path}\\rocketleague\\TAGame\\CookedPCConsole\\Labs_Utopia_P.upk"
            os.system("@echo off")
            os.system(f'echo "{desired_map}"')
            os.system(f'echo F|xcopy /y "{desired_map}" "{utopia_path}"')
            sg.popup_auto_close(auto_close_duration=0.2)

        else:
            sg.popup_error('No platform selected!', 'Please select a platform.')

window.close()

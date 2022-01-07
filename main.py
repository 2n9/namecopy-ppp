import PySimpleGUI as sg
import pyperclip
import pyautogui

sg.theme('Dark Blue 3')

layout = [ [sg.Text('Enter a Name')],
        [sg.InputText()],
        [sg.Button('Copy')] ]

window = sg.Window('Message Window', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Copy':
        name = values[0]
        base = "%NAME% aaa"
        pyperclip.copy(base.replace('%NAME%', name))
        sg.popup('Copied!')
window.close()

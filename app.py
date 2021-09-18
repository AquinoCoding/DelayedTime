import os
import PySimpleGUI as sg

def turnOff(): # Imediatamente para Desligar
    return os.system("shutdown /s /t /1")

def reIniti(): # Imediatamente para o Reinicio
    return os.system("shutdown /r /t /2")

def backLock(): # Imediatamente saindo 
        return os.system("shutdown -l")

layout = [
    [sg.B('Reiniciar', key='_reIniti_')],
    [sg.B('Desligar', key='_turnOff_')],
    [sg.B('Sair', key='_close_')],]

window = sg.Window('Delayed', layout, element_justification='center', size=(350,150))

event, values = window.read()

if event == sg.WIN_CLOSED:
    close()

elif event == '_reIniti_':
    reIniti()

elif event == '_turnOff_':
    turnOff()

elif event == '_close_':
    backLock()







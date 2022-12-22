import function_todo
import PySimpleGUI as PSG


label = PSG.Text("Type in a to-do")
input_box = PSG.InputText(tooltip='Enter a to-do')
add_button = PSG.Button("Add")

window = PSG.Window("My To-do App", layout=[[label,input_box, add_button]])

window.read()
window.close()
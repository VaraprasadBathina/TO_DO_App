from modules import functions
import FreeSimpleGUI as sg

label = sg.Text('Type In A To-Do')
input_box = sg.InputText(tooltip='Enter To-Do', key='todo')
add_button = sg.Button("ADD")

window = sg.Window('To-Do APP', 
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while(True):
    event, values  = window.read()
    print(event)
    print(values)
    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos_args=todos)

        case sg.WIN_CLOSED:
            break

window.close()


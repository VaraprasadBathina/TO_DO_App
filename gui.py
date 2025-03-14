from modules import functions
import FreeSimpleGUI as sg

label = sg.Text('Type In A To-Do')
input_box = sg.InputText(tooltip='Enter To-Do', key='todo')
add_button = sg.Button("ADD")
list_box = sg.Listbox(values = functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("EDIT")
complete_button = sg.Button("COMPLETE")
exit_button = sg.Button("EXIT")



window = sg.Window('To-Do APP', 
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                           ],  
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
            window['todos'].update(values=todos)
            """ Added ADD feature calling functions from module"""

        case "EDIT":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "COMPLETE":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value='')
        case "EXIT":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()


def get_todos(filepath = 'todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlinees()
    return todos_local
""" This Function is to Read a text file and 
return the list of To-Do Items"""


def write_todos(todos_args,filepath='todos.txt'):
    with open(filepath,'w') as local_file:
            local_file.writelines(todos_args)
""" This Function is to write To-Do items in the list to the text file"""
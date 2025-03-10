from modules import functions
import time

now  = time.strftime("(%a) %b %d %Y %H:%M:%S ")
print("It is ", now)

while True:
    user_action = input(" Select Add/Show/Edit/Complete/Exit: ")
    user_action = user_action.strip()

    if user_action.startswith('Add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos,filepath='todos.txt')


    elif user_action.startswith('Show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1} - {item}"
            print(row)

    elif user_action.startswith('Edit'):
        try:
            number = int(input(user_action[5:]))
            number = number-1

            todos = functions.get_todos()

            
            new_todo = input(" Enter New ToDo: ")
            todos[number]= new_todo + '\n'

            functions.write_todos(todos, filepath='todos.txt')

        except ValueError:
            print("Command is not Valid")
            continue



    elif user_action.startswith('Complete'):

        try:
            number = int(input(user_action[9:]))

            todos = functions.get_todos()

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, filepath='todos.txt')
            
            message = f"Removed the {todo_to_remove} ToDo from the List"
            print(message)
        except IndexError:
            print("There is no task with that number.")
            continue

    elif user_action.startswith('Exit'):
        break

print("Bye!")



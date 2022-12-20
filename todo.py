import function_todo
import time

now = time.strftime("%a %b %Y")
print(now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()         # remove unintentional space from input data/string

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = function_todo.get_todos()

        todos.append(todo + "\n")               # items add in the list

        function_todo.write_todos(todos)

    elif user_action.startswith("show"):

        todos = function_todo.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = function_todo.get_todos()

            new_todo = input("Enter a todo: ")
            todos[number] = new_todo

            function_todo.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = function_todo.get_todos()

            todos.pop(number-1)

            function_todo.write_todos(todos)
        except IndexError:
            print("Index out of range")
            continue

    elif "exit" in user_action:
        break
    else:
        print("Command is not valid.")
print("So long loser")

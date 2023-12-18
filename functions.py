FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    """ This Functions reads the  lists
    That are writen.
    """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILEPATH):
    """ This function writes the Todo list"""
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())

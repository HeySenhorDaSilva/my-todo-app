FILEPATH_TODO = "todos.txt"
FILEPATH_NAME= "naming.txt"  # uppercase shows that it is meant as a constant
def get_todos(filepath=FILEPATH_TODO):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:  # öffnet die file
        todos_local = file_local.readlines()  # speichert die Items in der File in ne Liste
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH_TODO):
    """ write a to-do items list in the text file."""
    with open(filepath, 'w') as file:  # öffnet die file
        file.writelines(todos_arg)  # schreibt die neue Liste rein


def write_names(name_arg, filepath=FILEPATH_NAME):
    with open(filepath, 'w') as file_name:  # öffnet die file
        file_name.writelines(name_arg)  # schreibt die neue Liste rein
    return name_arg


def read_names(filepath=FILEPATH_NAME):
    with open(filepath, 'r') as file_name:  # öffnet die file
        name_local = file_name.readlines()  # speichert die Items in der File in ne Liste
    return name_local

if __name__ =="__main__":
    print(get_todos())

    #last change before merge
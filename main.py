import sys
from create import create
from delete import delete
from list import get_list


# taking arguments amount
if len(sys.argv) < 2:
    print('not enough arguments')
    exit()

# take arguments
_, command, *args = sys.argv


# our commands to run function
commands = {
    'create': create,
    'delete': delete,
    'list': get_list,
}

# run requests
if command not in commands:
    print('command is incorrect')
    exit()
commands[command](*args)


import sys
from delete import delete
from create import create
from list import get_list, show_help


# taking arguments amount
if len(sys.argv) < 2:
    print('not enough arguments')
    exit()

# take arguments
_, command, *args = sys.argv



# our commands to run function
commands = {
    'help': show_help,
    'list': get_list,
    'create': create,
    'delete': delete,
}

# run requests
if command not in commands:
    print('command is incorrect')
    exit()
commands[command](*args)


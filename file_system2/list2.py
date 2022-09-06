import os
from pprint import pp
from pathlib import Path
# file with paths to directories
from path import directory
import pickle
from path import file_s_place
from create import create_hash
import time


# getting files list
nl = []


def get_list():
    if not os.path.exists(file_s_place):
        take_list = []
        with open(file_s_place, 'wb') as f:
            dir_list = os.listdir(directory)

            for file_name in dir_list:
                file_path = os.path.join(directory, file_name)
                file_size = os.stat(file_path).st_size

                take_list.append(
                    {
                        'name': file_name,
                        'size': file_size,
                        'hash': create_hash(file_name)
                    }
                )
            pickle.dump(take_list, f)
            print(take_list)

    else:
        with open(file_s_place, 'rb') as f:
            saved_list = pickle.load(f)
            print(saved_list)



    # start = time.time()
    # file_list = os.listdir(f_list)
    # for file in file_list:
    #     file_size = os.stat(os.path.join(f_list, file)).st_size
    #     print(f'name: {file}, size: {file_size} bytes')
    #     print(file)
    # print(start - time.time())




# commands for helping
def show_help() -> None:
    help_commands = {
        'copy_file': 'create <file_name>',
        'delete_file': 'delete <file_name>',
        'file_list': 'list',
    }
    pp(help_commands)


import os
import pickle5 as pickle
from create import create_hash, create_db
from path import file_s_place, directory

# deleting files
def delete(*args) -> None:
    file_name = args[0]
    list_d = []

    if file_name not in os.listdir(directory):
        print('file does not exist')
    else:
        join = os.path.join(directory, file_name)
        file_size = os.stat(os.path.join(directory, file_name)).st_size
        create_db(file_name, file_size, list_d, create_hash(file_name))
        os.remove(join)
        print("file deleted")




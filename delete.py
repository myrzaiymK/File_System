import os
import pickle5 as pickle
from config import directory
from create import create_hash


def delete(*args):
    file = args[0]
    hash_string = create_hash(file)
    hash_head, hash_tail = hash_string[:4], hash_string[4:]
    cursor = os.path.join(directory, 'cache')

    for dir_name in hash_head:
        dir_path = os.path.join(cursor, dir_name)

        if os.path.exists(dir_path):
            cursor = dir_path

            new_cursor = os.path.join(cursor, 'files')
            if os.path.exists(os.path.join(new_cursor, file)):
                os.remove(os.path.join(new_cursor, file))
                names = os.path.join(cursor, 'names.data')
                content = os.path.join(cursor, 'content.data')
                global_file = os.path.join(directory, 'global_file.data')
                update_files(names)
                update_files(content)
                update_files(global_file)



def update_files(file):
    new_data = []
    with open(file, 'rb') as f:
        load_data = pickle.load(f)
        for items in load_data:
            if str(file) in items:
                del items[str(file)]
                new_data.append(load_data)
    with open(file, 'wb') as nf:
        pickle.dump(new_data, nf)
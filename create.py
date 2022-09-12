import os
import hashlib
import time
import pickle5 as pickle
from config import directory
from open_file import read_file, write_to_file, add_to_file, create_file


def create(*args):
    file = args[0]
    hash_string = create_hash(file)
    hash_head, hash_tail = hash_string[:4], hash_string[4:]
    cursor = os.path.join(directory, 'cache')

    for dir_name in hash_head:
        dir_path = os.path.join(cursor, dir_name)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            cursor = dir_path
            continue

        cursor = dir_path

    content_data(file, cursor)
    open_global_file(cursor)


def create_hash(file_name):
    file_name_hash = hashlib.sha3_256(file_name.encode()).hexdigest()
    return file_name_hash


def open_file_rb(file):
    with open(file, 'rb') as read_file:
        data = pickle.load(read_file)
        return data


def open_global_file(cursor):
    content_file = open_file_rb(os.path.join(cursor, 'content.data'))
    names_file = open_file_rb(os.path.join(cursor, 'content.data'))
    with open(os.path.join(directory, 'global_file.data'), 'ab') as f:
        pickle.dump((content_file, names_file), f)


def content_data(file_name, cursor):
    names_list = []
    content_list = []
    new_cursor = names_data(cursor, file_name, names_list)

    with open(os.path.join(cursor, 'content.data'), 'wb') as f:
        file_size = os.stat(os.path.join(new_cursor, file_name)).st_size
        created_time = time.time()
        content_dict = create_table(file_name, file_size, created_time)
        content_list.append(content_dict)
        pickle.dump(content_list, f)
    file = os.path.join(cursor, 'content.data')
    open_file_rb(file)


def names_data(cursor, file_name, names_list):
    names_file = os.path.join(cursor, 'names.data')
    file_name_hash = create_hash(names_file)
    names_list.append(file_name_hash)
    write_to_file(names_list, names_file)

    new_cursor = os.path.join(cursor, 'files')
    if not os.path.exists(new_cursor):
        os.mkdir(new_cursor)
        pass
    file_path = os.path.join(new_cursor, file_name)
    create_file(file_path)
    return new_cursor


def create_table(file: str, size: int, data: float) -> None:
    data = {
        'file_name': file,
        'data': data,
        'size': size,
    }
    return data



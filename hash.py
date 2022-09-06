import os
from pickle5 import pickle

directory = "/Users/myrzaiym/Documents/Projects/file_system/Dir"
path = '/Users/myrzaiym/Documents/Projects/file_system/names_example.data'


with open(path, 'r') as f:
    hashes = []
    file_content = f.readlines()
    for line in file_content:
        file = hashes.append(line)

for hash_string in hashes:
    hash_head, hash_tail = hash_string[:4], hash_string[4:]
    cursor = os.path.join(directory, 'cache')

    for dir_name in hash_head:
        dir_path = os.path.join(cursor, dir_name)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        cursor = dir_path

    file_path = os.path.join(cursor, hash_string)

    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(hash_string, f)
    else:
        with open(file_path, 'rb') as f:
            file_data = pickle.load(f)

        with open(file_path, 'wb') as f:
            new_data = file_data + '\n' + 'hash_string'
            pickle.dump(new_data, f)



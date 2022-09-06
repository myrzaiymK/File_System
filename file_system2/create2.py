import os
import shutil
import hashlib
import pickle5 as pickle
from path import files_dir, directory, file_s_place


# function to create and copy file
def create(*args):
    if not args:
        exit()

    file = args[0]
    n_list = []

    if file not in os.listdir(directory):
        open(os.path.join(files_dir, file), "w")
        shutil.copy2(os.path.join(files_dir, file), directory)
        file_size = os.stat(os.path.join(files_dir, file)).st_size
        file_hash = create_hash(file)
        # print(hash1)
        create_db(file, file_size, n_list, file_hash)
        # sort_by_hash().setdefault(file)

        print("file  copied")
    else:
        print('file already exists')


def create_hash(file):
    hash1 = hashlib.md5(file.encode('utf-8'))
    file_hash = hash1.hexdigest()
    return file_hash


def create_db(file, file_size, n_list, file_hash):
    dict_f = {
        'name': file,
        'bytes': file_size,
        'hash': file_hash,
    }
    n_list.append(dict_f)
    f = open(file_s_place, 'rb')
    list_d = list(pickle.load(f))
    list_d.append(dict_f)
    pickle.dump(list_d, open(file_s_place, 'wb'))
    print(list_d)

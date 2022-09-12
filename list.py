import os
import fnmatch
import pickle5 as pickle
from config import directory, file_system

file_path = os.path.join(directory, 'global_file.data')


def get_list():
    with open(file_path, 'rb') as f:
        a = pickle.load(f)
        print(a)

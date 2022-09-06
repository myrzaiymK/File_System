import itertools
import os
import pickle
# from path import directory

directory = "/Users/myrzaiym/Documents/Projects/file_system/Dir/"

# root = '/home/myrzaiym/zeon_fs2/abc/index/files_/'

hash_chars = tuple('0123456789abcdef')

x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
permutations = [p for p in itertools.product(x, repeat=4)]

for i in permutations:
    filename = directory + '/'.join(i) + '/files.pickle'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'wb') as file:
        pickle.dump({}, file)

# print(permutations)
# os.makedirs('dir4')




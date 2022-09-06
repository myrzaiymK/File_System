import os
import pickle5 as pickle
from path import file_s_place, directory
import hashlib
from create import create_hash
import sys
# print(hashlib.algorithms_guaranteed)

# _, command, *args = sys.argv
a = 'dfghjkl'
for i in os.listdir(directory):
    hash1 = create_hash(i)

h = hashlib.md5(file_s_place.encode('utf-8'))
a = h.hexdigest()

count = 0
l = []
while count < 100:
    file = str(count) + '.txt'
    size = 0
    dict_f = {
        'name': file,
        'bytes': size,
        'hash': hash1,
    }
    count += 1
    l.append(dict_f)
# print(l)

with open(file_s_place, 'wb') as f:
    pickle.dump(l, f)

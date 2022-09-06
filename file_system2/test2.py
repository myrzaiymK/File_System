import os
# import pickle
import pickle5 as pickle
from pickle import *

# import file_list
file = '/Users/myrzaiym/Documents/Projects/file_system/file_test'

# count = 0
# list = []
# while count < 5:
#     file = str(count)
#     with open(os.path.join(files, file), "w") as f:
#         f.write('a')
#     list.append(file)
#     count += 1


# with open('file_list.py', 'a') as file_l:
#     list_str = str(list)
#     file_l.write(list_str)
# print(list)
stru = str('qwertyuiop')
pickle.dump(stru, open(file, 'wb'))
y = pickle.load(open(file))
print(y)



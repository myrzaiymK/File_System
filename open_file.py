import pickle5 as pickle


def create_file(file):
    f = open(file, 'wb').close()
    return f


def read_file(file):
    with open(file, 'rb') as f:
        pickle.load(f)


def write_to_file(data, file):
    with open(file, 'wb') as f:
        pickle.dump(data, f)


def add_to_file(data, file):
    with open(file, 'ab') as f:
        pickle.dump(data, f)
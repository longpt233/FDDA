import os

def create_if_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f'Path \'{path}\' just created!')
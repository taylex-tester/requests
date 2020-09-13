import os


def get_base_path():
    pwd = os.path.dirname(os.path.abspath(__file__))
    path = os.path.dirname(pwd)
    return path


base_path = get_base_path()


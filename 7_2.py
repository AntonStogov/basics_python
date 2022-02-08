import os
from os import path, makedirs
import yaml

with open(r'C:\Python3\Project1\lesson_7\config.yaml') as file:
    config_dir = yaml.full_load(file)

def create_dir(values, prefix=""):
    for directory, paths in values.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_dir(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    create_dir(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass
create_dir(config_dir)
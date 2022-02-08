from os import path, makedirs

my_dict = {'my_project_0': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}
for key, value in my_dict.items():
    if not path.exists(key):
        for n in value:
            for i in n.keys():
                makedirs(path.join(key, i))
    else:
        print('Каталог уже создан')






"""

import yaml
with open(r'C:\Python3\Project1\lesson_7\config.yaml') as file:
    config_dir = yaml.full_load(file)
    for i, n in config_dir.items():
        print(i, ';', n)
        
"""

"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp


Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); 
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
 можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
 
"""
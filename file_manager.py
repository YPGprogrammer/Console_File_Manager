import os
import shutil
import sys


def filemanagerfunc(user_input):
    if user_input == 1:
        user_name = str(input('Введите название папки: '))
        os.mkdir(user_name)
    elif user_input == 2:
        user_name = str(input('Введите название папки/файла: '))
        shutil.rmtree(user_name)
    elif user_input == 3:
        user_name = str(input('Введите название папки/файла: '))
        copy = user_name + '-copy'
        if os.path.isdir(user_name):
            shutil.copytree(user_name, copy)
        else:
            shutil.copyfile(user_name, copy)
    elif user_input == 4:
        output = os.listdir()
        print(output)
    elif user_input == 5:
        direct = []
        curr_dir = os.getcwd()
        content = os.listdir(curr_dir)
        for dirs in content:
            if os.path.isdir(os.path.join(curr_dir, dirs)):
                direct.append(dirs)
        print(direct)
    elif user_input == 6:
        files = []
        curr_dir = os.getcwd()
        content = os.listdir(curr_dir)
        for file in content:
            if os.path.isfile(os.path.join(curr_dir, file)):
                files.append(file)
        print(files)
    elif user_input == 7:
        print(sys.platform)

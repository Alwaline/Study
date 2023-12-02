import os
import shutil


def check_dir(path):
    return os.path.exists(path)


def see_dir(path):
    for root, directories, files in os.walk(path):
        print(root)
        for directory in directories:
            print(directory)
        for file in files:
            print(file)
    print('---------------------------')

def make_dir(path_dir):
    os.mkdir(path_dir)

def del_dir_file(path):
    os.rmdir(path)

def copy_file(path_1, path_2):
    shutil.copyfile(path_1, path_2)

def move_file(path_1, path_2):
    os.replace(path_1, path_2)

def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            print(os.path.join(root, name))

def mod_file(path):
    os.chmod(path, 777)

def main():
    # Содержимое текущей директории
    see_dir(os.getcwd())

    # Создание новой директории
    make_dir(os.getcwd()+'\\test')

    see_dir(os.getcwd())

    # удаление директории
    del_dir_file(os.getcwd()+'\\test')

    see_dir(os.getcwd())
    
    # копирование файла
    copy_file(os.getcwd()+'\\main.py', os.getcwd()+'\\main123.txt')

    see_dir(os.getcwd())

    # переиещение файла
    move_file(os.getcwd()+'\\main123.txt', os.getcwd()+'\\папка\\main123.txt')

    see_dir(os.getcwd())

    # поиск файла в текущей и подпапках
    find_file('12345.txt', '.')

    # Изменение доступа к файлу
    mod_file(os.getcwd()+'\\папка\\main123.txt')



if __name__ == "__main__":
    main()
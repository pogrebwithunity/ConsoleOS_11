import os

def command():
    print('Создание папки')
    a = input('Имя папки: ')
    os.system(f'mkdir {a}')
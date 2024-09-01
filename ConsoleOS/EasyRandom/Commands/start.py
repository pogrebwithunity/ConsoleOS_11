import os
def command():
    a = input('Что надо заупстить (файл - f, файл Python - fp): ')
    if a == 'f':
        b = input('Имя файла (с .расширение): ')
        os.system(f'start {b}')
    if a == 'fp':
        b = input('Имя файла Python (с .py, .pyw): ')
        os.system(f'py {b}')
    
        
def restart():
    
    os.system('cls')
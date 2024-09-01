def command():
        print('Создание нового файла')
        a = input('Имя файла: ')
        b = input('Текст файла: ')
        f = open(a, 'w+')
        f.write(b)
        f.close()
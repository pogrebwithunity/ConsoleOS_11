import EasyRandom
import time
import os

def command():
            print('Очистка всего')
            time.sleep(EasyRandom.randomIntByRange(5, 10))
            os.remove('file.sys')
            print('Удаление file.sys')
            time.sleep(EasyRandom.randomIntByRange(5, 10))
            os.remove('console.sys')
            print('Удаление console.sys')
            time.sleep(EasyRandom.randomIntByRange(5, 10))
            os.remove('timeModule.sys')
            print('Удаление timeModule.sys')
            time.sleep(EasyRandom.randomIntByRange(5, 10))
            os.remove('EasyRandomModule.sys')
            print('Удаление EasyRandomModule.sys')
            time.sleep(EasyRandom.randomIntByRange(5, 10))
            print('Переустановка системы "Console", это может занять много времени.')
            time.sleep(EasyRandom.randomIntByRange(12, 24))
            f = open('file.sys', 'w+')
            g = open('console.sys', 'w+')
            h = open('timeModule.sys', 'w+')
            j = open('EasyRandomModule.sys', 'w+')

            f.close()
            g.close()
            h.close()
            j.close()
            os.system('cls')
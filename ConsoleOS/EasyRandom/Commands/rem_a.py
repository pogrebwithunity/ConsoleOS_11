import EasyRandom
import os
import time

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
            time.sleep(5)
            os.system('cls')
            time.sleep(5)    
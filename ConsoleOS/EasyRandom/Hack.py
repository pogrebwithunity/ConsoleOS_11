import time
import EasyRandom
import os

import EasyRandom.Commands
import EasyRandom.Commands.help
import EasyRandom.Commands.mkdir
import EasyRandom.Commands.nwf
import EasyRandom.Commands.rem_a
import EasyRandom.Commands.rem_a_r
import EasyRandom.Commands.start

f = open('file.sys', 'w+')
g = open('console.sys', 'w+')
h = open('timeModule.sys', 'w+')
j = open('EasyRandomModule.sys', 'w+')

f.close()
g.close()
h.close()
j.close()

def StartConsole():
    print('Запуск Console')
    time.sleep(EasyRandom.randomIntByRange(1, 5))

    def Console():
        a = input('User_Console > ')
        
        if a == 'help':
            EasyRandom.Commands.help.command()
            Console()

        if a == "nwf":
            EasyRandom.Commands.nwf.command()
            Console()
            
        if a == 'mkdir':
            EasyRandom.Commands.mkdir.command()
            Console()
            
        if a == 'rem -a -r':
            EasyRandom.Commands.rem_a_r.command()
            Console()
            
        if a == 'start':
            EasyRandom.Commands.start.command()
            Console()
            
        if a == 'restart':
            EasyRandom.Commands.start.restart()
            Console()

        if a == 'rem -a':
            a = input('Введите пароль > ')
            if a == '12345':
                EasyRandom.Commands.rem_a.command()
                exit()

        if a == 'su':
             a = input('Введите пароль > ')
             if a == '12345':
                 b = input('Root_Console > ')

                 if b == 'rem -a -r':
                    EasyRandom.Commands.rem_a_r.command()
                    Console()

                 if b == 'rem -a':
                    EasyRandom.Commands.rem_a.command()
                    exit()

             else:
                 print('Пароль неверный')
                 Console()
        else:
            Console()
    Console()

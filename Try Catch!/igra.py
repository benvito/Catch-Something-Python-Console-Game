import random as rn
from colorama import Fore, Back, Style, init
import colorama
import emoji
import os
import keyboard
import time
from tqdm import tqdm
from termcolor import colored
init()

def restart():
    if input('Вы хотите начать заново? да/нет >>> ').lower() == 'да':
        if input('Вы выбрать конфигурацию заново? да/нет >>> ').lower() == 'да':
            os.system('cls')
            vibor()
            mapGen()
            printGame()
        else:
            mapGen()
            printGame()
    else:
        print(colored('Спасибо что сыграл!', 'magenta'))
        time.sleep(2)
        exit()

def vibor():
    global slog
    global skin
    skin = int(input('Выберите скин(1 - ʕᵔᴥᵔʔ, 2 - (⌐■_■), 3 - (^ω^), 4 - (¬_¬), 5 - (u_u)) >>> '))
    slog = int(input('Выберите сложность(1 - easy, 2 - medium, 3 - hard, 4 - impossible) >>> '))

    global kolvo
    global hod
    global x
    global y
    global x2
    global y2
    global hoda
    global n
    global xxx
    global yyy
    global player
    global probel

    if slog == 1:
        xxx = 4
        yyy = 7
        hoda = 12

    elif slog == 2:
        xxx = 6
        yyy = 9
        hoda = 18

    elif slog == 3:
        xxx = 9
        yyy = 12
        hoda = 23

    elif slog == 4:
        xxx = 15
        yyy = 22
        hoda = 28

    hod = hoda

    if skin == 1:
        player = 'ʕᵔᴥᵔʔ'
        probel = '     '
    if skin == 2:
        player = '(⌐■_■)'
        probel = '      '
    if skin == 3:
        player = '(^ω^)'
        probel = '     '
    if skin == 4:
        player = '(¬_¬)'
        probel = '     '
    if skin == 5:
        player = '(u_u)'
        probel = '     '


def mapGen():
    global x
    global y
    global x2
    global y2
    global kolvo
    global n
    global xxx
    global yyy
    global hod
    global hoda

    kolvo = 0
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    n = []
    for i in range(yyy):
        r = []
        for j in range(xxx):
            r.append(probel)
        n.append(r)
    n[y][x] = player

    for i in range(3):
        y2 = rn.randint(0,yyy-1)
        x2 = rn.randint(0, xxx-1)
        if y2 == 0 and x2 == 0:
            y2 += 1
        if skin == 1:
            n[y2][x2] = '  Ֆ  '
        if skin == 2:
            n[y2][x2] = '   Ֆ  '
        if skin == 3:
            n[y2][x2] = '  Ֆ  '
        if skin == 4:
            n[y2][x2] = '  Ֆ  '
        if skin == 5:
            n[y2][x2] = '  Ֆ  '

    if slog == 1:
        xxx = 4
        yyy = 7
        hoda = 12

    elif slog == 2:
        xxx = 6
        yyy = 9
        hoda = 18

    elif slog == 3:
        xxx = 9
        yyy = 12
        hoda = 23

    elif slog == 4:
        xxx = 15
        yyy = 22
        hoda = 28
    hod = hoda

vibor()
mapGen()

def printGame():
    os.system('cls')
    print('▬' * (xxx * 6))
    for i in n:
        print('▓',i, '▓')
    print('▬' * (xxx * 6))

printGame()

def gameLoop():
    for i in range(hod):
        #v = input('● ● ● Введите W, A, S или D для предвижения >>> ')
        global oo
        oo = False
        global hoda
        hoda -=1
        global kolvo
        kolvo = 0
        global y
        global x
        while True:
            try:
                if keyboard.is_pressed('w') == True and oo == False:
                    n[y][x] = probel
                    y-=1
                    if y < 0:
                        y = yyy - 1
                    n[y][x] = player
                    oo = True
                    break

                if keyboard.is_pressed('s') == True and oo == False:
                    n[y][x] = probel
                    y+=1
                    if y >= yyy:
                        y = 0
                    n[y][x] = player
                    oo = True
                    break

                if keyboard.is_pressed('a') == True and oo == False:
                    n[y][x] = probel
                    x-=1
                    if x < 0:
                        x = xxx - 1
                    n[y][x] = player
                    oo = True
                    break

                if keyboard.is_pressed('d') == True and oo == False:
                    n[y][x] = probel
                    x+=1
                    if x > xxx-1:
                        x = 0
                    n[y][x] = player
                    oo = True
                    break
            except:
                break


        mylist = [1, 2, 3, 4, 5, 6, 7, 8]

        for i in tqdm(mylist):
            time.sleep(0.05)
        os.system('cls')

        print('▬' * (xxx * 6))
        for i in n:
            print('▓', i, '▓')
        print('▬' * (xxx * 6))

        for j in n:
            for k in j:
                if k == '  Ֆ  ' or k == '   Ֆ  ' or k == emoji.emojize('  Ֆ '):
                    kolvo += 1

        print(colored(f'● ● ● Ходов осталось: {hoda}', 'yellow'))

        print(colored(f'▐ ▐ Ֆ осталось >>> {kolvo} ▐ ▐', 'yellow'))

        if kolvo == 0:
            for i in range(10):
                print(colored('░▒▓█░▒▓█░▒▓█░▒▓█ ПОБЕДА █▓▒░█▓▒░█▓▒░█▓▒░\n', 'magenta'))
            print(colored('░▒▓█░▒▓█░▒▓█░▒▓█ ПОБЕДА █▓▒░█▓▒░█▓▒░█▓▒░\n >>> ', 'magenta'))
            os.system('pause')
            restart()

        if hoda == 0:
            for i in range(10):
                print(colored('█▒▒▒▒▒▒▒█ Ходы закончились, попробуйте снова █▒▒▒▒▒▒▒█\n', 'red'))
            print(colored('█▒▒▒▒▒▒▒█ Ходы закончились, попробуйте снова █▒▒▒▒▒▒▒█\n >>> ', 'red'))
            os.system('pause')
            restart()

while True:
    gameLoop()



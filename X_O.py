from random import randrange as rnd
import time
import sys

count = 0

def Thinking():
    proces = rnd(20,70)
    for i in range(proces):
        time.sleep(0.1)
        sys.stdout.write("\rДумаю.....: %d%%" % i)
        sys.stdout.flush()
    print('\n')

def print_matrix(st):
    for i in range(len(st)):
        for j in range(len(st[i])):
            print(st[i][j],end=' ')
        print()
def fill_matrix(st,a=None,b=None):
    if a is None and b is None:
        while True:
            a = rnd(0,3)
            b = rnd(0,3)
            if st[a+1][b+1] =='_':
                st[a + 1][b + 1] = 'o'
                print('Ход компьютера.......')
                #Thinking()
                break
    else:
        st[a+1][b+1] = 'x'
    print_matrix(st)
def chek_winner(st,player):
    for i in range(1,4):
        if st[i][1] == st[i][2] == st[i][3]==player or st[1][i] == st[2][i] == st[3][i]==player:
            return True
        elif st[1][1] ==st[2][2] ==st[3][3]==player or st[1][3] ==st[2][3] ==st[1][3]==player:
            return True
        else:
            return False

def call_counter(func):
    def wrapper(*args):
        global count
        func(*args)
        count += 1
        print(f"Вы сыграли {count} раз, может еще раз?")
    return wrapper




@call_counter
def x_and_0(st):
        print('******Будем вводить целые цифры от 0 включительно до 2 включительно********')
        print_matrix(st)
        while True:
            fill_matrix(st,int(input('Введите номер строки = ')), int(input('Ввудите номер колонки =')))
            player = 'x'
            if chek_winner(st,player):
                print('Вы выиграли!! УРА!!!!')
                break
            fill_matrix(st)
            player = 'o'
            if chek_winner(st, player):
                print('Вы проиграли!!')
                break




while input('Хотите сыграть в крестики-нолики? (Y|N)') == 'Y':
    matrix = [
        [' ', 0, 1,2],
        [0, '_', '_','_'],
        [1, '_', '_','_'],
        [2, '_', '_','_']]
    m_matrix = matrix.copy()
    x_and_0(m_matrix)













import random
from tkinter import *
from Interface import *

__all__ = ['jogar_Dados', 'window2', 'confCanvas2']

'''
def selecionar_Jogada():

def soma_Dados():

def proximo_Jogador():

def manter_Dados():
'''
root = window()
w = confCanvas()

def window2():
    global root
    return root

def confCanvas2():
    global w
    return w

dados = [0,0,0,0,0]

img = [PhotoImage(file="dado_1.png"), PhotoImage(file="dado_2.png"), PhotoImage(file="dado_3.png"),
           PhotoImage(file="dado_4.png"), PhotoImage(file="dado_5.png"), PhotoImage(file="dado_6.png")]

def jogar_Dados():
    global dados
    global root
    global w
    for i, k in enumerate(dados):
        dados[i] = random.randint(1, 6)
    print('Verificacao lista de dados: {}'.format(dados))
    desenha_dado_iniciais()
    return dados

def desenha_dado_iniciais():
    global img
    global w
    x = 180
    for el in dados:
        w.create_image(x, 600, anchor=NW, image=img[el - 1])
        x = x + 40
    return


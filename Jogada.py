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
'''
def desenha_dado_iniciais():
    global img
    global root
    global dados
    img = [PhotoImage(file="dado_1.png"), PhotoImage(file="dado_2.png"), PhotoImage(file="dado_3.png"),
           PhotoImage(file="dado_4.png"), PhotoImage(file="dado_5.png"), PhotoImage(file="dado_6.png")]
    botao_dos_dados1 = Button(root, image=img[dados[0] - 1])
    botao_dos_dados1.place(x=340, y=550)
    botao_dos_dados2 = Button(root, image=img[dados[1] - 1])
    botao_dos_dados2.place(x=300, y=550)
    botao_dos_dados3 = Button(root, image=img[dados[2] - 1])
    botao_dos_dados3.place(x=260, y=550)
    botao_dos_dados4 = Button(root, image=img[dados[3] - 1])
    botao_dos_dados4.place(x=220, y=550)
    botao_dos_dados5 = Button(root, image=img[dados[4] - 1])
    botao_dos_dados5.place(x=180, y=550)
    return
'''
def desenha_dado_iniciais():
    global img
    global root
    global dados
    img = [PhotoImage(file="dado_1.png"), PhotoImage(file="dado_2.png"), PhotoImage(file="dado_3.png"),
           PhotoImage(file="dado_4.png"), PhotoImage(file="dado_5.png"), PhotoImage(file="dado_6.png")]
    dado1 = Label(root, image=img[dados[0] - 1]).pack(side=LEFT)
    dado2 = Label(root, image=img[dados[1] - 1]).pack(side=LEFT)
    dado3 = Label(root, image=img[dados[2] - 1]).pack(side=LEFT)
    dado4 = Label(root, image=img[dados[3] - 1]).pack(side=LEFT)
    dado5 = Label(root, image=img[dados[4] - 1]).pack(side=LEFT)
    return


def jogar_Dados():
    global dados
    global root
    global w
    for i, k in enumerate(dados):
        dados[i] = random.randint(1, 6)
    desenha_dado_iniciais()
    return dados

import random
from tkinter import *
from Interface import *
import Tabela as tabelaArq

__all__ = ['jogar_Dados', 'window2', 'confCanvas2']

'''
def selecionar_Jogada():
def soma_Dados():
def proximo_Jogador():
def manter_Dados():
'''

root = window()
w = confCanvas()

x_mouse = 0
y_mouse = 0

dados = [0,0,0,0,0]
dadosMantidos = [0,0,0,0,0]

img = [PhotoImage(file="dado_1.png"), PhotoImage(file="dado_2.png"), PhotoImage(file="dado_3.png"),
           PhotoImage(file="dado_4.png"), PhotoImage(file="dado_5.png"), PhotoImage(file="dado_6.png")]
botaoFoto = PhotoImage(file="botao.png")

def window2():
    global root
    return root

def confCanvas2():
    global w
    return w

def callback(event):
    global dadosMantidos
    global x_mouse
    global y_mouse
    
    x_mouse = event.x
    y_mouse = event.y

    if x_mouse > 180 and x_mouse < 212 and y_mouse>550 and y_mouse<582:
        if dadosMantidos[0] == 0:
            dadosMantidos[0] = 1
            w.create_rectangle(180, 550, 212, 582, outline = 'black', tag = 'ret1')
        else:
            dadosMantidos[0] = 0
            w.delete('ret1')
    
    if x_mouse > 220 and x_mouse < 252 and y_mouse>550 and y_mouse<582:
        if dadosMantidos[1] == 0:
            dadosMantidos[1] = 1
            w.create_rectangle(220, 550, 252, 582, outline = 'black', tag = 'ret2')
        else:
            dadosMantidos[1] = 0
            w.delete('ret2')
    
    if x_mouse > 260 and x_mouse < 292 and y_mouse>550 and y_mouse<582:
        if dadosMantidos[2] == 0:
            dadosMantidos[2] = 1
            w.create_rectangle(260, 550, 292, 582, outline = 'black', tag = 'ret3')
        else:
            dadosMantidos[2] = 0
            w.delete('ret3')
    
    if x_mouse > 300 and x_mouse < 332 and y_mouse>550 and y_mouse<582:
        if dadosMantidos[3] == 0:
            dadosMantidos[3] = 1
            w.create_rectangle(300, 550, 332, 582, outline = 'black', tag = 'ret4')
        else:
            dadosMantidos[3] = 0
            w.delete('ret4')
    
    if x_mouse > 340 and x_mouse < 372 and y_mouse>550 and y_mouse<582:
        if dadosMantidos[4] == 0:
            dadosMantidos[4] = 1
            w.create_rectangle(340, 550, 372, 582, outline = 'black', tag = 'ret5')
        else:
            dadosMantidos[4] = 0
            w.delete('ret5')

    if x_mouse > 240 and x_mouse < 320 and y_mouse>600 and y_mouse<630:
        if tabelaArq.jogadasFeitas < 2:
            jogar_Dados()
            tabelaArq.atualizaDpsDeManter()
            w.delete('ret1')
            w.delete('ret2')
            w.delete('ret3')
            w.delete('ret4')
            w.delete('ret5')
        else:
            print("Numero de jogadas maximo atingido, favor escolha uma pontuacao.")
        controleRodadas()

    print("Coordenadas: ", event.x, event.y, "\n")

def desenha_dado_iniciais():
    global img
    global root
    global dados
    global w
    x = 180
    for el in dados:
        w.create_image(x, 550, anchor=NW, image=img[el - 1])
        x = x + 40
    return


'''
def manterDados():
    global dados
    global dadosMantidos
    global jogadasFeitas
    if jogadasFeitas < 3:
        for i, k in enumerate(dados):
            if dadosMantidos[i] == 1:
                dados[i] = random.randint(1, 6)
        desenha_dado_iniciais()
        jogadasFeitas += 1
    else:
        print("Numero de jogadas maximas atingido")
    print(dadosMantidos)
    dadosMantidos = [0,0,0,0,0]
    return dados
'''

def controleRodadas():
    global dadosMantidos
    
    dadosMantidos = [0,0,0,0,0]
    return

def jogar_Dados():
    global dados
    global root
    global w
    global dadosMantidos
    
    for i, k in enumerate(dados):
        if dadosMantidos[i] == 0:
            dados[i] = random.randint(1, 6)
    
    desenha_dado_iniciais()
    
    ###
    w.create_image(240, 600, anchor=NW, image=botaoFoto)
    w.create_text(280,500,fill="white",font='algerian',text="Clique nos dados que gostaria de manter")
    w.bind("<Button 1>", callback)
    ###

    return dados

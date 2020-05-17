import random
from tkinter import *

__all__ = ['jogar_Dados']

'''
def selecionar_Jogada():

def soma_Dados():

def proximo_Jogador():

def manter_Dados():
'''
dados = [0,0,0,0,0]

def jogar_Dados():
    global dados
    for i,k in enumerate(dados):
        dados[i] = random.randint(1,6)
    '''
    canvas = Canvas(width=400, height=250, bg='blue')   
    
    img = []
    img.append(PhotoImage(file="dado_1.png"))
    img.append(PhotoImage(file="dado_2.png"))
    img.append(PhotoImage(file="dado_3.png"))
    img.append(PhotoImage(file="dado_4.png"))
    img.append(PhotoImage(file="dado_5.png"))
    img.append(PhotoImage(file="dado_6.png"))
    
    
    x=30
    for el in dados:
        canvas.create_image(x,100, anchor=NW, image=img[el-1])
        x = x + 40
    canvas.pack()
    '''
    
    return dados





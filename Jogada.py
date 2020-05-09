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
    return dados





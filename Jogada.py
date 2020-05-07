import random
from tkinter import *
__all__ = ['jogar_Dados']

'''
def selecionar_Jogada():

def soma_Dados():

def proximo_Jogador():

def manter_Dados():
'''

def jogar_Dados(dados):
    for i,k in enumerate(dados):
        dados[i] = random.randint(1,6)
    return dados



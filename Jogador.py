from tkinter import *

__all__ = ['desenhaJogador', 'criaJogador']

'''
def escolherNome():
'''

def criaJogador():
    tabela = {
     'ones':None, 
     'twos':None,
     'threes':None,
     'fours':None,
     'fives':None,
     'sixes':None,
     'bonus superior':None,
     'three of a kind':None,
     'four of a kind':None,
     'full house':None,
     'small straight':None,
     'large straight':None,
     'chance':None,
     'yahtzee':None,
     'bonus yahtzee':None,
     'total':None
     }
    return tabela

def desenhaJogador(root, w):
    h = 0
    i = 0
    w.create_rectangle(681, 0, 710, 700)
    while(i < 17):
        h += 43.75
        w.create_line(681, h, 710, h)
        i += 1
    return 0

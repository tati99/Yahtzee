from Pontuacao import *
from Jogada import *

def exibe(d):
     for k in d:
        print(k,':', d[k])


def main(tabela):
     d = []
     dados = [0,0,0,0,0]
     d = jogar_Dados(dados)
     tabela = mostrarOpcoes(d,tabela)
     exibe(tabela)

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

main(tabela)


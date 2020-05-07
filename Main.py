from tkinter import *
from Tabela import *
from Interface import *
from Jogada import *
from Pontuacao import *
from Jogador import *

def main():
     tabela = criaJogador()
     root = window()
     w = confCanvas()
     confCanvas()
     desenhaTabela(root,tabela,w)
     desenhaJogador(root, w)
     dados = [0,0,0,0,0]
     dados = jogar_Dados(dados)
     print(dados)
     dic = mostrarOpcoes(dados, tabela)
     criaOpcoes(dic, root, w, tabela)
     root.mainloop()
     return

main()
from tkinter import *
from Tabela import *
from Interface import *
from Jogada import *
from Pontuacao import *
from Jogador import *

#escolherNome()
root = window()
w = confCanvas()
root.title("Yahtzee")

def main():
     global root
     global w
     tabela = criaJogador()
     init(root, w)
     desenhaTabela(tabela)
     desenhaJogador(root, w)
     dados = jogar_Dados()
     print(dados)
     dic = mostrarOpcoes(dados, tabela)
     criaOpcoes(dic,tabela)
     root.mainloop()
     return

main()
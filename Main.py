from tkinter import *
from Tabela import *
from Interface import *
from Jogada import *
from Pontuacao import *
from Jogador import *

escolherNome()
root = window2()
w = confCanvas2()
root.title("Yahtzee")

def main():
     global w
     global root
     w.create_rectangle(20,13,1338,687, fill='green')
     tabela = criaJogador()
     desenhaTabela(tabela)
     desenhaJogador()
     jogaJogador()
     root.mainloop()
     return

main()
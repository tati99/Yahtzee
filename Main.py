from tkinter import *
from Tabela import *
from Interface import *
from Jogada import *
from Pontuacao import *
from Jogador import *

escolherNome()
root = window()
w = confCanvas()
root.title("Yahtzee")

def main():
     global root
     global w
     tabela = criaJogador()
     init(root, w)
     w.create_rectangle(20,13,1338,687, fill='green')
     desenhaTabela(tabela)
     desenhaJogador(root, w)
     #img = PhotoImage(file='dado_1.png')
     #w.create_image(250, 250, image=img)
     jogaJogador()
     root.mainloop()
     return

main()
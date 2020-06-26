from tkinter import *
from Tabela import *
from tkinter.filedialog import askopenfilename
import Tabela as tab
from ast import literal_eval

__all__ = ['desenhaJogador', 'criaJogador', 'escolherNome', 'jogaJogador']


jogador = []
e1 = 0
s = 0
root = window4()
w = confCanvas4()
b1 = 0
b2 = 0
add = 0
e = 0
s = list()
list_dict = list()

def escolherNome():
    global e1
    global root
    global w
    global b1
    global b2
    global add
    global e
    e = Label(root, text="Name", bg='white')
    e.place(x=50,y=100)
    e1 = Entry(root)
    e1.place(x=100,y=100)
    b1 = Button(root,text='Jogar',command=jogaJogador)
    b1.place(x=100,y=130)
    add = Button(root,text='Adicionar',command=entrada)
    add.place(x=240,y=97)
    b2 = Button(root, text="Carregar jogo",command=carregarJogo)
    b2.place(x = 240, y = 150)
    return

def carregarJogo():
    global b1
    global b2
    global e1
    global add
    global s
    k = 0
    arq = askopenfilename(defaultextension = '.txt')
    f = open(arq, 'r')
    if f is None:
        return
    for i in f:
        i = i.strip('\n')
        list_dict.append(literal_eval(i))

    b1.destroy()
    b2.destroy()
    e1.destroy()
    add.destroy()
    e.destroy()
    print(len(list_dict))
    for i in range(len(list_dict)):
        s.append('Jogador ' + str(i + 1))
        
    tabela = criaJogador()
    w.create_rectangle(20,13,1338,687, fill='green')
    desenhaTabela(tabela)
    desenhaJogador()
        
    criaOpcoes(list_dict)
    
    return
    

def jogaJogador():
    global b1
    global e1
    global add
    k = 0
    b1.destroy()
    e1.destroy()
    add.destroy()
    e.destroy()
    tabela = criaJogador()
    w.create_rectangle(20,13,1338,687, fill='green')
    desenhaTabela(tabela)
    desenhaJogador()
    size  = len(s)
    while (k < size):
        list_dict.append(criaJogador())
        k += 1
    criaOpcoes(list_dict)


def entrada():
    global e1
    global jogador
    global s
    s.append(e1.get().upper())
    s = s[0:10]

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

def desenhaJogador():
    global s
    global w
    h = 50
    i = 0
    for contador in range(0,len(s)):
        w.create_rectangle(681+69*contador, 15, 750+69*contador, 674, fill='white')
        w.create_text(716+69*contador,35,text=s[contador])
    for i in range(16):
        w.create_line(681, h, 680+69*len(s), h)
        h += 39
    return 0

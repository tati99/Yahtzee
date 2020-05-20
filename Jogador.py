from tkinter import *
from Tabela import *

__all__ = ['desenhaJogador', 'criaJogador', 'escolherNome', 'jogaJogador']

jogador = []
e1 = 0
s = 0
root = window4()
w = confCanvas4()

def escolherNome():
    global e1
    master = Tk()
    e = Label(master, text="Name")
    e.place(x=50,y=100)
    e1 = Entry(master)
    e1.place(x=100,y=100)
    b1 = Button(master,text='Play',command=master.quit)
    b1.place(x=100,y=130)
    add = Button(master,text='Add',command=entrada)
    add.place(x=240,y=97)
    master.mainloop()
    return

def jogaJogador():
    tabela = criaJogador()
    criaOpcoes(tabela)
    

def entrada():
    global e1
    global jogador
    global s
    s = e1.get()
    s = s[0:10]
    s = s.upper()

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
    w.create_rectangle(681, 15, 750, 674, fill='white')
    w.create_text(716,35,text=s)
    while(i < 16):
        w.create_line(681, h, 750, h)
        h += 39
        i += 1
    return 0

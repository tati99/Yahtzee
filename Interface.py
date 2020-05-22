from tkinter import *

__all__ = ['confCanvas', 'window']

root = 0

def window():
    global root
    root = Tk()
    return root

def confCanvas():
    global root
    w = Canvas(root, width=920, height=700, bg='white')
    button_quit = Button(root, padx=10, pady=10, text="Sair do Jogo", font='algerian', command=root.quit)
    w.pack()
    button_quit.pack()
    return w

'''
def alterar_Tela():

def arruma_Tabela():

def organizar_Jogadores():
'''
    

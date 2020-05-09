from tkinter import *

__all__ = ['confCanvas', 'window']

root = 0

def window():
    global root
    root = Tk()
    return root

def confCanvas():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    w = Canvas(root, width=screen_width, height=screen_height, bg='white')
    w.pack()
    return w

'''
def alterar_Tela():

def arruma_Tabela():

def organizar_Jogadores():
'''
    

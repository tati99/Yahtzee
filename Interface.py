from tkinter import *

__all__ = ['confCanvas', 'window', 'confTela']

root = 0

def window():
    global root
    root = Tk()
    return root

def confCanvas():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    w = Canvas(root, width=screen_width, height=screen_height)
    w.pack()
    return w

def confTela():
    return 0

'''
def alterar_Tela():

def arruma_Tabela():

def organizar_Jogadores():
'''
    

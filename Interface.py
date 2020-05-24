from tkinter import *
__all__ = ['confCanvas', 'window']

root = 0

def window():
    global root
    root = Tk()
    return root

def confCanvas():
    global root
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    w = Canvas(root, width=800, height=800, bg='white')
    button_quit = Button(root, text="Sair do Jogo", font='algerian', command=root.quit)
    w.pack()
    button_quit.pack()
    return w

'''
def alterar_Tela():

def arruma_Tabela():

def organizar_Jogadores():
'''
    

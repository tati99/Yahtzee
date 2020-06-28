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
    w = Canvas(root, width=screen_width, height=screen_height, bg='white')   
    button_quit = Button(root, text="Sair do Jogo", command=root.quit)
    w.pack()
    button_quit.place(x=1250, y=650)
    return w

    

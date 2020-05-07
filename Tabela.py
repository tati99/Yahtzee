from tkinter import *

__all__ = ['desenhaTabela', 'preencheTabela', 'criaOpcoes']

but = []
name = []
sp = []
w1 = 0
dic = dict()
dic_aux = dict()

def desenhaTabela(root, d, w):
   i = 0
   h = 0
   n = 0
   w.create_rectangle(600, 0, 681, 768)
   while(i < 17):
      h += 43.75
      w.create_line(600, h, 681, h)
      i += 1
   for i in d:
      w.create_text(640, (2*n+1)*21.875, text = i)
      n += 1
   return 

def criaOpcoes(d, root, w, tabela):
   global but
   global w1 
   global dic
   global name
   global dic_aux
   global sp 
   sp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
   dic = tabela.copy()
   dic_aux = d.copy()
   w1 = w
   h = 1
   z = 0
   j = 0
   for i in d:
      if (d[i]!=0 and d[i]!=-1 and d[i]!=None):
         z += 1
   if (z > 0):
      for i in d:
         if(d[i]!=-1 and d[i]!=None and d[i]!=0):
            b = Button(root, width=2, height=2, text=str(d[i]), fg='red', command= lambda: buttonClick)
            but.append(b)
            b.place(x=683, y=h)
            b.bind("<Button-1>", buttonClick)
            name.append(i)
            sp[j] = -1
         h += 43.75
         j += 1
   else:
      for i in d:
         if(d[i]!=-1 and d[i]!=None):
            b = Button(root, width=2, height=2, text=str(d[i]), fg='red', command= lambda: buttonClick)
            but.append(b)
            b.place(x=683, y=h)
            b.bind("<Button-1>", buttonClick)
            name.append(i)
            sp[j] = -1
         h += 43.75
         j += 1
   return

def buttonClick(event):
   global but
   global name
   global dic_aux
   global sp
   j = 0
   i = 0
   k = 0
   for button in but:
      if button is event.widget:
         n = j
         s = button['text']
      j += 1
   while (i < len(but)):
      but[i].destroy()
      i += 1
   p = n
   for i in dic_aux:
      if (i == name[p]):
         break
      k += 1
   w1.create_text(695, (2*k+1)*21.875, text = s)
   preencheTabela(name[p], s)


def preencheTabela(v, s):
   dic[v] = int(s)
   return dic








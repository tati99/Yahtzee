from tkinter import *

__all__ = ['desenhaTabela', 'preencheTabela', 'criaOpcoes', 'init', 'desenhaPontos']

but = []
name = []
sp = []
dic = dict()
dic_aux = dict()
root = 0
w = 0

def init(window, ca):
   global root
   global w
   root = window
   w = ca

def desenhaPontos(d):
   global w 
   global root
   k = 0
   for i in d:
      if d[i] != None:
         w.create_text(714, 50+(2*k+1)*19.5, text = str(d[i]))
      k += 1

def desenhaTabela(d):
   global w
   global root
   i = 0
   h = 50
   n = 0
   w.create_rectangle(600, 50, 681, 674, fill='white')
   while(i < 17):
      w.create_line(600, h, 681, h)
      h += 39
      i += 1
   for i in d:
      s = i
      s = s.capitalize()
      w.create_text(640, 50+(2*n+1)*19.5, text = s)
      n += 1
   return 

def criaOpcoes(d,tabela):
   global but
   global dic
   global name
   global dic_aux
   global sp
   global root 
   sp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
   dic = tabela.copy()
   dic_aux = d.copy()
   h = 58
   z = 0
   j = 0
   for i in d:
      if (d[i]!=0 and d[i]!=-1 and d[i]!=None):
         z += 1
   if (z > 0):
      for i in d:
         if(d[i]!=-1 and d[i]!=None and d[i]!=0):
            b = Button(root, width=5, height=1, text=str(d[i]), fg='red', bg='white',command= buttonClick)
            but.append(b)
            b.place(x=692, y=h)
            b.bind("<Button-1>", buttonClick)
            name.append(i)
            sp[j] = -1
         h += 39
         j += 1
   else:
      for i in d:
         if(d[i]!=-1 and d[i]!=None):
            b = Button(root, width=5, height=1, text=str(d[i]), fg='red', bg='white', command= buttonClick)
            but.append(b)
            b.place(x=692, y=h)
            b.bind("<Button-1>", buttonClick)
            name.append(i)
            sp[j] = -1
         h += 39
         j += 1
   return

def buttonClick(event):
   global but
   global name
   global dic_aux
   global sp
   global dic
   global w
   j = 0
   i = 0
   k = 0
   dic_atu = dict()
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
   w.create_text(714, 50+(2*k+1)*19.5, text = s)
   dic_atu = preencheTabela(name[p], s)
   if (s=='100' or s =='200' or s=='300'):
      joker()
   
def preencheTabela(v, s):
   dic[v] = int(s)
   return dic

def joker():
   global sp
   dic_aux2 = dict()
   dic_aux2 = dic_aux.copy()
   dic_aux2['bonus yahtzee'] = -1
   for i in dic_aux2:
      if dic_aux2[i]!=None and dic_aux2[i]!=0 and dic_aux2[i]!=-1:
         break
   for i,j in enumerate(sp):
      if j==-1:
         break
   if i<7:
      dic_aux2['three of a kind'] = -1
      dic_aux2['four of a kind'] = -1
      dic_aux2['chance'] = -1
   else:
      dic_aux2[i] = -1
   criaOpcoes(dic_aux2,dic)
   
      


   









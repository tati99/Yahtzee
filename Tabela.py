from tkinter import *
from tkinter import filedialog
from Pontuacao import *

__all__ = ['desenhaTabela', 'preencheTabela', 'criaOpcoes', 'window4', 'confCanvas4', 'atualizaDpsDeManter']

but = []
name = []
sp = []
dic = dict()
dic_aux = dict()
root = 0
w = 0
cont = 0
ld = list()
jogadasFeitas = 0
partida = 0
teste = 0
check = False
root = window3()
w = confCanvas3()
checkJoker = False
dic_ant = dict()
b3 = 0
coroa = PhotoImage(file="coroa.png")
def window4():
    global root
    return root

def confCanvas4():
    global w
    return w

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

def save_file():
    global dic
    content = list()
    file_name = filedialog.asksaveasfilename(defaultextension = '.txt')

    f = open(file_name, 'w')
    if f is None:
        return
    for i in ld:
        f.write(str(i))
        f.write('\n')
    f.close()
    return

def criaOpcoes(tabela):
   global but
   global dic
   global name
   global dic_aux
   global sp
   global root 
   global w
   global ld
   global partida
   global check
   global checkJoker
   global dic_ant
   global b3
   global coroa
   if (checkJoker == True):
      dic_ant = ld[partida-1]
   ld = tabela.copy()
   sp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
   if (check == True):
      partida -= 1
   if (partida == (len(ld))):
      partida = 0
   if (checkJoker==True):
      partida -= 1
   dic = ld[partida].copy()
   if (checkJoker==False):
      d = mostrarOpcoes(dic)
   else:
      d = dic
   dic_aux = d.copy()
   h = 58
   z = 0
   j = 0
   k = 0
   t = 0
   partida += 1

   b2 = Button(root, text="Save as", command = save_file)
   b2.place(x = 25, y = 20)
   
   for i in d:
      if (d[i]!=0 and d[i]!=-1 and d[i]!=None):
         z += 1
   for i in dic:
      if dic[i] == None:
         k += 1
   if k == 3:
      while (t < len(ld)):
         dic_f = somaColuna(ld[t])
         w.create_text(714+70*t, 50+(2*6+1)*19.5, text = str(dic_f['bonus superior']), tag="bonussuperior")
         w.create_text(714+70*t, 50+(2*15+1)*19.5, text = str(dic_f['total']), tag="total")
         if dic_f['bonus yahtzee'] == 0:
            w.create_text(714+70*t, 50+(2*14+1)*19.5, text = '–',tag="bonusyahtzee")
         t += 1
      t = 1
      pos = 0
      aux3 = ld[0]["total"]
      while (t < len(ld)):
         if (ld[t]["total"]>aux3):
            aux3 = ld[t]["total"]
            pos += 1
         t += 1
      w.create_image(699+69*pos, 5, anchor=NW, image=coroa, tags="coroa")
      b3 = Button(root, width=7, height=1, text="Reiniciar", fg='black',command= reiniciar)
      b3.place(x=1258, y=608)
   if (z > 0):
      for i in d:
         if(d[i]!=-1 and d[i]!=None and d[i]!=0):
            b = Button(root, width=5, height=1, text=str(d[i]), fg='red', bg='white',command= buttonClick)
            but.append(b)
            b.place(x=692+70*(partida-1), y=h)
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
            b.place(x=692+70*(partida-1), y=h)
            b.bind("<Button-1>", buttonClick)
            name.append(i)
            sp[j] = -1
         h += 39
         j += 1
   return 

def atualizaDpsDeManter():
    global but
    global dic
    global jogadasFeitas
    global ld
    global partida
    global check
    i = 0
    while (i < len(but)):
        but[i].destroy()
        i += 1
    jogadasFeitas += 1

    if jogadasFeitas == 1:
        w.delete("texto_2jogadas")
        w.create_text(290, 650, fill="white", font='algerian', text="Você possui 1 jogada disponível !", tag="texto_1jogadas")
    if jogadasFeitas == 2:
        w.delete("texto_1jogadas")
        w.create_text(290, 650, fill="white", font='algerian', text="Você nao possui mais jogadas !", tag="sem_jogadas")
    check = True
    ld[partida - 1] = dic.copy()
    criaOpcoes(ld)
    
def buttonClick(event):
   global but
   global name
   global dic_aux
   global sp
   global dic
   global w
   global cont
   global jogadasFeitas
   global teste
   global ld
   global partida
   global check
   global checkJoker
   check = False
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
   w.create_text(714+70*(partida-1), 50+(2*k+1)*19.5, text = s, tag="numero")
   dic_atu = preencheTabela(name[p], s)
   if (s=='100' or s =='200' or s=='300'):
      joker()
   checkJoker = False
   w.delete("texto_1jogadas")
   w.delete("sem_jogadas")
   jogadasFeitas = 0
   teste = 1
   ld[partida-1] = dic_atu.copy()
   criaOpcoes(ld)

def preencheTabela(v, s):
   global dic_ant
   global checkJoker
   dic[v] = int(s)
   return dic

def joker():
   global sp
   global partida
   global dic_aux
   global checkJoker
   ld_aux = [0,0,0,0,0,0]
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
   checkJoker = True
   ld_aux[partida-1] = dict()
   ld_aux[partida-1] = dic_aux2.copy()
   criaOpcoes(ld_aux)

def reiniciar():
   global ld
   global b3
   global coroa
   w.delete("numero")
   w.delete("bonussuperior")
   w.delete("total")
   w.delete("bonusyahtzee")
   w.delete("coroa")
   b3.destroy()
   for i,k in enumerate(ld):
      for j in ld[i]:
         ld[i][j] = None
   criaOpcoes(ld)




   
   









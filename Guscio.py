import sys
import math
from Punto import Punto

#lettura di una lista di punti da un file      
def lettura_punti(nome_file):
    file = open(nome_file)
    n = file.read()  
    lista = n.split()
    punti = []
    try:
      for i in range(0,len(lista),2):
        p = Punto(float(lista[i]),float(lista[i+1]))
        punti.append(p) #aggiunta elemento in fondo alla lista
      file.close()
      return punti
    #gestione eccezioni
    except (ValueError):
      print("Errore nella lettura di un numero")
    except (IndexError):
      print("Errore: il file deve contenere un numero pari di numeri")
#lettura dei punti dal file indicato
lista_punti = lettura_punti(sys.argv[1])
#gestione errori
if len(lista_punti)<3:
  raise IndexError("Errore: numero di punti non sufficiente")

#calcolo le coordinate del baricentro
nbaricentrox=0 
nbaricentroy=0 
for p in lista_punti:
   nbaricentrox=p.x+nbaricentrox
   nbaricentroy=p.y+nbaricentroy
Punto.baricentrox=nbaricentrox/len(lista_punti)
Punto.baricentroy=nbaricentroy/len(lista_punti)

#ordinamento radiale della lista
lista_punti.sort()

#metodo per individuare il punto più distante dal baricentro
def puntoMaxDistanza(L):
  maxP = L[0]
  for p in L[1:]:
    if p.distanza()>maxP.distanza():
      maxP = p
  return maxP

#metodo per ordinare la lista in modo radiale a partire dal punto più distante dal baricentro    
def ordl(L):
  a=L.index(puntoMaxDistanza(L))
  return L[a:]+L[:a] #ritorna una nuova lista ordinata
L=ordl(lista_punti)

#metodo per individuare l'orientamento di una terna di punti
def orient(a, b, c):
    return (c.x-a.x)*(b.y-a.y)-(c.y-a.y)*(b.x-a.x)

  #metodo per controllare se i punti della lista possono appartenere al guscio convesso
  # def checkLista(L):
  #   if len(L)==3:
  #     return L
  
# def guscioconv(L):
# 		guscio = []
# 		guscio.append(L[0])
# 		for p in L:
# 			guscio.append(p)
# 			while len(guscio) > 2 and orient(guscio[-3],guscio[-2],guscio[-1])<0:
# 				guscio.pop(-2)
# 		return guscio
# guscioconv(L)

def guscioconv(lista_punti):
  guscio = []
  orientati = ordl(lista_punti)
  for p in orientati:
    # if we turn clockwise to reach this point, pop the last point from the stack, else, append this point to it.
    while len(guscio) > 1 and orient(guscio[-2], guscio[-1], p)>=0:
      guscio.pop()
    guscio.append(p)
  # the stack is now a representation of the convex guscio, return it.
  return guscio

L=guscioconv(L) 

#file di scrittura
file_output = open(sys.argv[2],'w')
for p in L:
  file_output.write(str(p))
  file_output.write('\n')
file_output.close()


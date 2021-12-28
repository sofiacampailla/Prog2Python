import sys
from Punto import Punto
#metodi che utilizza il main per trovare i punti appartenenti al guscio convesso
#metodo per individuare il punto più distante dal baricentro
def puntoMaxDistanza(L):
  maxP = L[0]
  for p in L[1:]:
    if p.distanza()>maxP.distanza():
      maxP = p
  return maxP

#metodo per ordinare la lista in modo da partire dal punto più distante dal baricentro    
def ordl(L):
  a=L.index(puntoMaxDistanza(L))
  return L[a:]+L[:a]

#metodo per individuare l'orientamento di una terna di punti
def orient(a, b, c):
    return (c.x-a.x)*(b.y-a.y)-(c.y-a.y)*(b.x-a.x)

#metodo per individuare i punti del guscio convesso
def guscioconv(lista_punti):
  guscio = []
  for p in lista_punti:
    while len(guscio) > 1 and orient(guscio[-2], guscio[-1], p)>=0:
      guscio.pop()
    guscio.append(p)
  #ritorna il guscio convesso
  return guscio


#lettura di una lista di punti da un file      
def lettura_punti(nome_file):
    file = open(nome_file)
    n = file.read()  
    lista = n.split() 
    punti = [] 
    try: 
      for i in range(0,len(lista),2): 
        p = Punto(float(lista[i]),float(lista[i+1]))
        punti.append(p)
      file.close()
      return punti
    #gestione eccezioni
    except (ValueError):
      print("Errore nella lettura di un numero")
    except (IndexError):
      print("Errore: il file deve contenere un numero pari di numeri")

##### main #####

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

#ordinamento radiale della lista fatta da oggetti della classe Punto
lista_punti.sort()

#applicazione metodo alla lista L
L=ordl(lista_punti)

#file di scrittura
file_output = open(sys.argv[2],'w')
for p in guscioconv(L): 
  file_output.write(str(p))
  file_output.write('\n')
file_output.close()


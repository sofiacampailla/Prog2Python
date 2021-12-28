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
    #se l'orientamento della svolta è a destra o i punti sono allineati
    #elimino l'ultimo punto dalla lista, altrimenti aggiungo il punto ad essa
    while len(guscio) > 1 and orient(guscio[-2], guscio[-1], p)>=0:
      guscio.pop()
    guscio.append(p) #al ciclo 0 e 1 non fa nulla, al ciclo 2 inizio confronto tra 3 punti
  #ritorna il guscio convesso
  return guscio


#lettura di una lista di punti da un file      
def lettura_punti(nome_file):
    file = open(nome_file)
    n = file.read()  
    lista = n.split() #divide ogni riga con spazio
    punti = [] #crea lista vuota 
    try: 
      for i in range(0,len(lista),2): #creo ogni punto con x e y
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
#per ogni elemento della lista di punti, calcolo somma x e somma y e divido per len per trovare baricentro
for p in lista_punti:
   nbaricentrox=p.x+nbaricentrox
   nbaricentroy=p.y+nbaricentroy
Punto.baricentrox=nbaricentrox/len(lista_punti)
Punto.baricentroy=nbaricentroy/len(lista_punti)

#ordinamento radiale della lista fatta da oggetti della classe Punto
#la classe Punto implementa l'operatore less than (__lt__)
#che permette di confrontare due oggetti Punto
#il metodo permette di confrontare due punti con < in mezzo
#il metodo sort della lista python chiama l'operatore < per ogni elemento della lista
lista_punti.sort()

#applicazione metodo alla lista L
L=ordl(lista_punti)

#file di scrittura
file_output = open(sys.argv[2],'w')
for p in guscioconv(L): #per ogni punto del guscio convesso trovato, scrivo su file
  file_output.write(str(p))
  file_output.write('\n')
file_output.close()


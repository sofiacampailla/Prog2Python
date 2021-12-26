import sys
import math

class Punto:
  baricentrox = 1
  baricentroy = 1

  def   __init__ (self,x=0.0,y=0.0):
      self.x = x
      self.y = y
      
  def distanza(self):
        return ((self.x-Punto.baricentrox)**2 + (self.y-Punto.baricentroy)**2)**(0.5)

  def angolo(self):
      if self.distanza()==0: return 0
      angolo = math.acos((self.x-Punto.baricentrox)/self.distanza())
      if self.y-Punto.baricentroy < 0: angolo = math.pi*2 - angolo
      return angolo
      
  def __str__(self):
      return str(self.x) + " " + str(self.y) 
      
  def __lt__(self,other):
      if self.angolo()==other.angolo(): return self.distanza()<other.distanza()
      return self.angolo()<other.angolo()
      
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
    except (ValueError):
      print("Errore nella lettura di un numero")
    except (IndexError):
      print("Errore: il file deve contenere un numero pari di numeri!")

lista_punti = lettura_punti(sys.argv[1])

nbaricentrox=0 
nbaricentroy=0 
for p in lista_punti:
   nbaricentrox=p.x+nbaricentrox
   nbaricentroy=p.y+nbaricentroy
Punto.baricentrox=nbaricentrox/len(lista_punti)
Punto.baricentroy=nbaricentroy/len(lista_punti)
lista_punti.sort()
file_output = open(sys.argv[2],'w')
for p in lista_punti:
  file_output.write(str(p))
  file_output.write('\n')
file_output.close()


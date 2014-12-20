from ListaStudenti import *
from Menu import *

def f1():
	print ("Funzione 1")

def f2():
	print ("Funzione 2")

m = Menu()
m.AggiungiVoce(1, "Aggiungi nuovi studenti", f1)
m.AggiungiVoce(0, "ESCI", f2)

m.MostraScelte()
m.Scegli()
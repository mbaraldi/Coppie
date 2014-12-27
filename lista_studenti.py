from lista_persone import ListaPersone
from studente import Studente
import random

class ListaStudenti(ListaPersone):
	""" Lista di studenti, derivata dalla lista di persone generiche """
	
	def __init__(self):
		ListaPersone.__init__(self)

	def Nuovo(self, nome, cognome):
		s = Studente(nome, cognome)
		self.lista.append(s)

	def CaricaCompagni(self):
		n = 3
		m= 0
		for st in self.lista:
			st.AggiungiCompagno(n)
			st.AggiungiCompagno(m)
			n -= 1
			m += 1

	def StampaCoppie(self):
		for st in self.lista:
			compagni = st.getListaCompagni()
			a = st.getNomeCognome()
			s = "{0} e' stato in banco con:".format(a)
			print(s)
			for c in compagni:
				comp = self.lista[c].getNomeCognome()
				comp = "- {0}".format(comp)
				print(comp)
			print('\n')

	def GeneraCoppie(self):
		nuova_lista = []
		#numero di compagni (tutti tranne lo studente stesso)
		ncomp = len(self.lista) - 1
		print("n. compagni: " + str(ncomp))
		i = 0
		for stud in self.lista:
			print('*'*30)
			#crea la lista di tutti i compagni
			tlista = []
			for n in range (0, ncomp + 1):
				#escludendo lo studente stesso
				if n != i:
					tlista.append(n)
			print("compagni di {0}: {1}".format(i, tlista))
			#elenco dei compagni con cui e' gia' stato in banco
			comp = stud.getListaCompagni()
			print ("gia stato con: " + str(comp))
			da_provare = ncomp
			trovato = False
			while not trovato:
				print("compagni ancora da provare: " + str(da_provare))
				pos = random.randrange(0, da_provare)
				c = tlista[pos]
				print("ho provato con: {}".format(c))
				if c in comp:
					print("c'era gia':")
					print(tlista)
					tlista.remove(c)
					print("tolto:")
					print(tlista)
					da_provare -= 1
				else:
					nuova_lista.append(c)
					trovato = True
					print("trovato!")
			i += 1
		print('*'*50)
		print (nuova_lista)
		print ("\n")
		i = 0
		for st in self.lista:
			a = st.getNomeCognome()
			b = self._Lista[nuova_lista[i]].getNomeCognome()
			s = "{0} va in banco con {1}".format(a, b)
			print(s)
			i += 1





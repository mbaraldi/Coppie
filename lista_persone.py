from persona import Persona
from os import path
import pickle

class ListaPersone(object):
	""" gestisce una lista di oggetti Persona, caricandoli e salvandoli su file
	"""
	def __init__(self):
		self._Lista = []
		self._file = ".\data.pkl"

	def Nuovo(self, nome, cognome):
		p = Persona(nome, cognome)
		self._Lista.append(p)

	def Aggiungi(self):
		print ("Aggiungi nuove persone ('x' per finire)")
		continua = True
		while continua:
			nome = input("Nome: ")
			if nome == "x" or nome == "":
				continua = False
			else:
				cognome = input("Cognome: ")
				if cognome == "x" or cognome == "":
					continua = False
				else:
					self.Nuovo(nome, cognome)
	
	def Rimuovi(self):
		print ("Rimuovi una persona ('0' per uscire)")
		elem = int(input("Elimina la persona numero: "))
		if elem == 0:
			print ("nessuna persona eliminata")
		elif elem < len(self._Lista):
			self._Lista.pop(elem-1)
		else:
			print ("{0} non e' un elemento valido".format(elem))

	def Ordina(self):
		print ("Ordina le persone per cognome e nome")
		risp = input("Vuoi riordinare la lista? (s/n) ")
		if risp == "s":
			self._Lista = sorted(self._Lista, key=lambda elem: elem.getCognomeNome())
			self.Stampa(20)
		else:
			print ("Ordinamento annullato")
		print("\n")

	def Salva(self):
		pickle.dump(self._Lista, open(self._file, "wb"))

	def Carica(self):
		if path.isfile(self._file):
			self._Lista = pickle.load(open(self._file, "rb"))
		else:
			self._Lista = []

	def Stampa(self, largh= 20):
		t = Persona("Nome", "Cognome")
		t.StampaHeader(largh)
		riga = 1
		for p in self._Lista:
			p.Stampa(riga, largh)
			riga += 1
		t.StampaFooter(largh)

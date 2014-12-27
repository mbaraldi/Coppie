from persona import Persona
from stampa_elenco import StampaElenco

from os import path
import pickle

class ListaPersone(object):
	""" gestisce una lista di oggetti Persona, caricandoli e salvandoli su file
	"""
	def __init__(self):
		self.lista = []
		self._file = ".\data.pkl"

	def Nuovo(self, nome, cognome):
		p = Persona(nome, cognome)
		self.lista.append(p)

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
		elif elem < len(self.lista):
			self.lista.pop(elem-1)
		else:
			print ("{0} non e' un elemento valido".format(elem))

	def Ordina(self):
		self.lista = sorted(self.lista)
	
	def Salva(self):
		pickle.dump(self.lista, open(self._file, "wb"))

	def Carica(self):
		if path.isfile(self._file):
			self.lista = pickle.load(open(self._file, "rb"))
		else:
			self.lista = []
		print ("Caricati {0} elementi".format(len(self.lista)))

	def Stampa(self):
		st = StampaElenco(["Nome", "Cognome"], 15)
		lista = []
		for stud in self.lista:
			lista.append([stud.nome, stud.cognome])
		st.CaricaLista(lista)
		st.Stampa()
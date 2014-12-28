from persona import Persona
from archiviatore import Archiviatore

class ListaPersone(object):
	""" gestisce una lista di oggetti Persona, caricandoli e salvandoli su file
	"""
	def __init__(self):
		self.lista = [] #lista di persone
		self.archivio = Archiviatore()

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
	
	def Carica(self, file = "data"):
		self.lista = self.archivio.Carica(file)

	def Salva(self, file = ""):
		self.archivio.Salva(self.lista, file)

	def getListaDaStampare(self):
		lista = []
		lista.append(["Nome", "Cognome"])
		for elem in self.lista:
			lista.append([elem.nome, elem.cognome])
		return lista

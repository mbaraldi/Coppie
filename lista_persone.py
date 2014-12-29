from persona import Persona
from archiviatore import Archiviatore

class ListaPersone(object):
	""" gestisce una lista di oggetti Persona, caricandoli e salvandoli su file
	"""
	def __init__(self):
		self.lista = [] #lista di persone
		self.archivio = Archiviatore()
		self.npersone = 0

	def Nuovo(self, nome, cognome):
		p = Persona(nome, cognome)
		self.lista.append(p)
		self.npersone += 1

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
	
	def Rimuovi(self, indice = 0):
		if indice > 0:
			elem = indice
		else:
			print ("Rimuovi una persona (da 1 a {0})".format(self.npersone))
			elem = int(input("Elimina la persona numero: "))
		if elem < 1 or elem > self.npersone:
			print ("{0} non e' un elemento valido".format(elem))
		else:
			self.lista.pop(elem-1)

	def Ordina(self):
		self.lista = sorted(self.lista)
	
	def Carica(self, file = "data"):
		self.lista = self.archivio.Carica(file)
		self.npersone = len(self.lista)

	def Salva(self, file = ""):
		self.archivio.Salva(self.lista, file)

	def getElemento(self, indice):
		if indice < 1 or indice > self.npersone:
			print ("{0} non e' un elemento valido".format(indice))
			ret = ""
		else:
			ret = self.lista[indice - 1].getNomeCognome()
		return ret

	def getListaDaStampare(self):
		lista = []
		lista.append(["Nome", "Cognome"])
		for elem in self.lista:
			lista.append([elem.nome, elem.cognome])
		return lista

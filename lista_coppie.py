from coppia import Coppia
from archiviatore import Archiviatore

class ListaCoppie(object):
	"""gestisce una lista di coppie di persone"""
	def __init__(self):
		self.lista = []
		self.archivio = Archiviatore()

	def Nuovo(self, primo, secondo):
		cp = Coppia(primo, secondo)
		self.lista.append(cp)

	def Carica(self, file = "data"):
		self.lista = self.archivio.Carica(file)

	def Salva(self, file = ""):
		self.archivio.Salva(self.lista, file)

	def getListaDaStampare(self):
		lista = []
		lista.append(["Persona 1", "Persona 2"])
		for coppia in self.lista:
			lista.append([coppia.primo.getNomeCognome(), coppia.secondo.getNomeCognome()])
		return lista


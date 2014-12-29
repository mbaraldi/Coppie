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

	def Aggiungi(self, lista):
		singol = {}
		for i, elem in enumerate(lista):
			singol[i+1] = elem.getNomeCognome()
		continua = True
		while continua:
			print ("Aggiungi nuove coppie ('0' per finire)")
			print("lista di persone non accoppiate:")
			for i in singol.keys():
				print ("{0:>2}) {1}".format(i, singol[i]))
			id1 = int(input("Id prima persona: "))
			if id1 == 0:
				continua = False
			else:
				print (singol[id1])
				id2 = int(input("Id seconda persona: "))
				if id2 == 0:
					continua = False
				elif id1 == id2:
					print("Si possono associare solo persone diverse")
				else:
					print (singol[id1] + " con " + singol[id2])
					self.Nuovo(lista[id1 - 1], lista[id2 - 1])
					del singol[id1]
					del singol[id2]
				print ("------")

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


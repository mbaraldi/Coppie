from os import path
import pickle

class Archiviatore(object):
	"""salva e carica oggetti su file binario, nella dir locale"""
	def __init__(self):
		self.file = "" #nome del file su cui salvare
		
	def Carica(self, file = "data"):
		self.file = file + ".pkl"
		if path.isfile(self.file):
			lista = pickle.load(open(self.file, "rb"))
		else:
			print (self.file)
			print ("File non trovato")
			lista = []
		print ("Caricati {0} elementi".format(len(lista)))
		return lista

	def Salva(self, lista, file = ""):
		if file > "": #salva su un altro file
			self.file = file + "\.pkl"
		pickle.dump(lista, open(self.file, "wb"))
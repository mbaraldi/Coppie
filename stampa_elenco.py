class StampaElenco(object):
	"""
	stampa a video una lista di liste di stringhe
	usando la prima riga come intestazione
	"""

	def __init__(self, largh = 20):
		self._nomiColonne = [] #titoli delle colonne, ricavati dalla prima riga della lista
		self._lista = [] #lista di valori da stampare
		self._ncolonne = 0 #numero di colonne
		self._largh = largh #larghezza delle colonne

	def _CaricaLista(self, lista):
		MAXCOLONNE = 5 #massimo numero di colonne gestite
		MAXLARGH = 70  #larghezza massima della tabella
		self._nomiColonne = []
		self._lista = []
		#prende solo il numero di colonne gestite dalla classe
		self._ncolonne = min(len(lista[0]), MAXCOLONNE)
		#adatta la larghezza al numero di colonne da stampare
		self._largh = min(self._largh, int(MAXLARGH/self._ncolonne))

		righe = 0
		for elem in lista:
			righe += 1
			tmp=[]
			for campo in elem:
				tmp.append(campo[:self._largh - 1])
			#la prima riga contiene le intestazioni di colonna
			if righe == 1:
				self._nomiColonne = tmp
			else:
				self._lista.append(tmp)

	def _Stampa(self):
		#riga vuota di separazione, usata sia nell'header che nel footer
		separatore = "|----"
		for i in range (0, self._ncolonne):
			separatore += "+{0}".format('-' * self._largh)
		separatore += "|"

		#riga di intestazione, con i nomi delle colonne
		intestazione = "|  # "
		#Aggiungo le altre colonne
		for col in self._nomiColonne:
			intestazione += "|{0:^{n}}".format(col, n = self._largh)
		intestazione += "|"

		#stampa l'header
		print(separatore)
		print(intestazione)
		print(separatore)

		#stampa il corpo della tabella
		nriga = 0
		for elem in self._lista:
			nriga += 1
			riga = "|{0:>3} ".format(nriga)
			for i in range (0, self._ncolonne):
				riga += "| {0:<{n}}".format(elem[i], n = self._largh - 1)
			riga += "|"
			print (riga)

		#stampa il footer
		print(separatore)

	def Stampa(self, lista):
		self._CaricaLista(lista)
		self._Stampa()


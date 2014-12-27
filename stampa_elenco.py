class StampaElenco(object):
	"""stampa a video una lista di oggetti"""

	def __init__(self, nomiColonne, largh = 20):
		#prende solo il numero di colonne gestite dalla classe
		MAXCOLONNE = 5 #massimo numero di colonne gestite
		MAXLARGH = 70  #larghezza massima della tabella
		self._nomiColonne = nomiColonne[:MAXCOLONNE]
		self._ncolonne = len(self._nomiColonne)
		self._largh = min(largh, int(MAXLARGH/self._ncolonne))
		self._lista = []

	def CaricaLista(self, lista):
		for elem in lista:
			tmp=[]
			for campo in elem:
				tmp.append(campo[:self._largh - 1])
			self._lista.append(tmp)

	def Stampa(self):
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



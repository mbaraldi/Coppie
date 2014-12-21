class MenuItem(object):
	"""
	Singola voce di menu, associata ad una funzione da chiamare
	"""
	def __init__(self, pos, descr, funz, esci):
		self._pos = pos 	#posizione nel menu
		self._descr = descr	#descrizione da mostrare
		self._funz = funz 	#funzione/metodo da richiamare
		self._esci = esci 	#uscire dopo l'esecuzione?
	
	def Esegui(self):
		self._funz()
		return self._esci
from persona import Persona

class Studente(Persona):
	""" Classe derivata, che gestisce anche la lista di compagni di banco
	"""
	def __init__(self, nome, cognome):
		Persona.__init__(self, nome, cognome)
		self._InBancoCon = []

	def AggiungiCompagno(self, num):
		self._InBancoCon.insert(0, num)

	def getListaCompagni(self):
		return self._InBancoCon
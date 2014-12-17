from Persona import Persona

class ListaPersone(object):
	"""
	gestisce una lista di oggetti Persona
	caricandoli e salvandoli su file
	"""
	def __init__(self):
		self._Lista = []

	def Aggiungi(self, nome, cognome):
		p = Persona(nome, cognome)
		self._Lista.append(p)

	def Carica(self):
		self.Aggiungi("Leonardo", "Baraldi")
		self.Aggiungi("Massimo", "Baraldi")
		self.Aggiungi("Elena", "Baraldi")
		self.Aggiungi("Mariangela", "Mandreoli")

	def Stampa(self, largh):
		t = Persona("Nome", "Cognome")
		t.StampaHeader(largh)
		for p in self._Lista:
			p.Stampa(largh)
		t.StampaFooter(largh)



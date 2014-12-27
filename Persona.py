class Persona(object):
	"""
	classe base per una persona generica
	"""
	def __init__(self, nome, cognome):
		self.nome = nome
		self.cognome = cognome

	def __str__(self):
		s = "nome:\t\t" + self.nome + "\ncognome:\t" + self.cognome
		return s
	
	def __lt__(self, other):
		minore = False
		if self.cognome < other.cognome:
			minore = True
		else:
			if self.cognome == other.cognome and self.nome < other.nome:
				minore = True
		return minore

	def getCognomeNome(self):
		return str(self.cognome + " " + self.nome)

	def getNomeCognome(self):
		return str(self.nome + " " + self.cognome)
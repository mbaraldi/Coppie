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
		c1 = self.cognome.lower()
		c2 = other.cognome.lower()
		n1 = self.nome.lower()
		n2 = other.nome.lower()

		minore = False
		if (c1 < c2 or (c1 == c2 and n1 < n2)):
			minore = True
		return minore

	def getCognomeNome(self):
		return str(self.cognome + " " + self.nome)

	def getNomeCognome(self):
		return str(self.nome + " " + self.cognome)
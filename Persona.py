class Persona(object):
	"""
	classe base per una persona generica
	"""
	def __init__(self, nome, cognome):
		self._nome = nome
		self._cognome = cognome

	def __str__(self):
		s = "nome:\t\t" + self._nome + "\ncognome:\t" + self._cognome
		return s
	
	def StampaHeader(self, largh):
		riga = "|-----+{0}+{0}|".format('-' * largh)
		s = "|  #  |{0:^{n}}|{1:^{n}}|".format(self._nome, self._cognome, n = largh)
		s = riga + "\n" + s + "\n" + riga
		print(s)

	def StampaFooter(self, largh):
		s = "|-----+{0}+{0}|".format('-' * largh)
		print(s)

	def Stampa(self, riga, largh):
		s = "|{0:^5}|{1:<{n}}|{2:<{n}}|".format(riga, self._nome, self._cognome, n = largh)
		print(s)

	def getNomeCognome(self):
		return str(self._nome + " " + self._cognome)

	def getCognomeNome(self):
		return str(self._cognome + " " + self._nome)


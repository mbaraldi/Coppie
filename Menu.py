from MenuItem import *

class Menu(object):
	"""
	Menu principale del programma

	"""
	def __init__(self):
		self._nvoci = 0
		self._menuItems = []

	def AggiungiVoce(self, pos, descr, funz, esci= False):
		self._nvoci += 1
		item = MenuItem(pos, descr, funz, esci)
		self._menuItems.append(item)

	def MostraScelte(self):
		testo = "Opzioni del menu:\n"
		for item in self._menuItems:
			testo += "{0:>2}) {1}\n".format(item._pos, item._descr)
		print (testo)

	def Scegli(self):
		esci = False
		while not esci:
			valida = False
			scelta = int(input("\nscegli una voce: "))
			for voce in self._menuItems:
				if scelta == voce._pos:
					valida = True
					esci = voce.Esegui()
					break
			if not valida:
				print ("Scelta non valida, prova ancora..")
				self.MostraScelte()
		print("Ciao!\n")
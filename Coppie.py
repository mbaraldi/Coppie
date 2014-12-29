from lista_studenti import ListaStudenti
from lista_coppie import ListaCoppie
from stampa_elenco import StampaElenco
from menu import Menu

studenti = ListaStudenti()
coppie = ListaCoppie()
stampe = StampaElenco(40)

def StampaStud():
	stampe.Stampa(studenti.getListaDaStampare())

def StampaCoppie():
	stampe.Stampa(coppie.getListaDaStampare())

def AggiungiCoppie():
	coppie.Aggiungi(studenti.lista)

def Esci():
	studenti.Salva()
	coppie.Salva()

studenti.Carica("data")
coppie.Carica("coppie")

m = Menu()
m.AggiungiVoce(1, "Stampa lista studenti", StampaStud)
m.AggiungiVoce(2, "Aggiungi nuovi studenti", studenti.Aggiungi)
m.AggiungiVoce(3, "Elimina uno studente dall'elenco", studenti.Rimuovi)
m.AggiungiVoce(4, "Ordina la lista di studenti", studenti.Ordina)
m.AggiungiVoce(5, "Aggiungi coppie", AggiungiCoppie)
m.AggiungiVoce(6, "Stampa coppie", StampaCoppie)
m.AggiungiVoce(9, "Mostra menu", m.MostraScelte)
m.AggiungiVoce(0, "ESCI", Esci, True)

m.MostraScelte()
m.Scegli()
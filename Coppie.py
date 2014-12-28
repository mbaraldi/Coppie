from lista_studenti import ListaStudenti
from stampa_elenco import StampaElenco
from menu import Menu

studenti = ListaStudenti()
studenti.Carica()

stampe = StampaElenco(40)
def StampaStud():
	stampe.Stampa(studenti.getListaDaStampare())

m = Menu()
m.AggiungiVoce(1, "Stampa lista studenti", StampaStud)
m.AggiungiVoce(2, "Aggiungi nuovi studenti", studenti.Aggiungi)
m.AggiungiVoce(3, "Elimina uno studente dall'elenco", studenti.Rimuovi)
m.AggiungiVoce(4, "Ordina la lista di studenti", studenti.Ordina)
m.AggiungiVoce(5, "Stampa coppie", studenti.StampaCoppie)
m.AggiungiVoce(9, "Mostra menu", m.MostraScelte)
m.AggiungiVoce(0, "ESCI", studenti.Salva, True)

m.MostraScelte()
m.Scegli()
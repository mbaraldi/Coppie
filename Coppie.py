from lista_studenti import ListaStudenti
from menu import Menu

Studenti = ListaStudenti()
Studenti.Carica()

m = Menu()
m.AggiungiVoce(1, "Stampa lista studenti", Studenti.Stampa)
m.AggiungiVoce(2, "Aggiungi nuovi studenti", Studenti.Aggiungi)
m.AggiungiVoce(3, "Elimina uno studente dall'elenco", Studenti.Rimuovi)
m.AggiungiVoce(4, "Ordina la lista di studenti", Studenti.Ordina)
m.AggiungiVoce(5, "Stampa coppie", Studenti.StampaCoppie)
m.AggiungiVoce(9, "Mostra menu", m.MostraScelte)
m.AggiungiVoce(0, "ESCI", Studenti.Salva, True)

m.MostraScelte()
m.Scegli()
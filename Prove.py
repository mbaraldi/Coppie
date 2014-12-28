from lista_studenti import ListaStudenti 
from lista_coppie import ListaCoppie
from stampa_elenco import StampaElenco

studenti = ListaStudenti()
coppie = ListaCoppie()
stampe = StampaElenco(40)

studenti.Carica("data")
studenti.Ordina()
stampe.Stampa(studenti.getListaDaStampare())

coppie.Nuovo(studenti.lista[0], studenti.lista[1])
coppie.Nuovo(studenti.lista[4], studenti.lista[2])
coppie.Nuovo(studenti.lista[3], studenti.lista[7])
coppie.Nuovo(studenti.lista[6], studenti.lista[5])
stampe.Stampa(coppie.getListaDaStampare())
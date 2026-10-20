import csv
from operator import attrgetter
from espositore import Espositore
from stand import Stand, StandPreseExtra, StandPremium

class LingottoFiere:
    """Inizializza gli attributi e le strutture dati"""
    """Aggiungere setter e getter se necessari"""
    def __init__(self, nome):
        self.__nome = nome
        self.__stand = {}
        self.__espositori = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        file = open(file_path, "r", encoding="utf-8")
        reader = csv.reader(file)

        for campi in reader:
            codice = campi[0]

            if codice.startswith("ES"):
                nome = campi[1]
                cognome = campi[2]
                nuovo_esp = Espositore(codice, nome, cognome)
                self.__espositori[codice] = nuovo_esp

            elif codice.startswith("ST"):
                sup = campi[1]
                pad = campi[2]
                prezzo = campi[3]

                if len(campi) == 4:
                    nuovo_stand = Stand(codice, sup, pad, prezzo)
                elif campi[4].isdigit():
                    prese = campi[4]
                    nuovo_stand = StandPreseExtra(codice, sup, pad, prezzo, prese)
                else:
                    pos = campi[4]
                    nuovo_stand = StandPremium(codice, sup, pad, prezzo, pos)

                self.__stand[codice] = nuovo_stand

        file.close()


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.__stand:
            raise ValueError("Stand non esistente.")
        if codice_espositore not in self.__espositori:
            raise ValueError("Espositore non esistente.")

        stand_scelto = self.__stand[codice_stand]
        espositore_scelto = self.__espositori[codice_espositore]

        if not stand_scelto.disponibile:
            raise ValueError("Lo stand selezionato non è disponibile.")
        if espositore_scelto.stand is not None:
            raise ValueError("L'espositore ha già uno stand associato.")

        stand_scelto.disponibile = False
        stand_scelto.espositore = espositore_scelto
        espositore_scelto.stand = stand_scelto

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.__espositori.values():
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # Ordina gli oggetti leggendo il valore della property 'prezzo'
        return sorted(self.__stand.values(), key=attrgetter("prezzo"))

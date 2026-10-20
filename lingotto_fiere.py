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
        lettore = csv.reader(file)

        for riga in lettore:
            if not riga:
                continue

            codice = riga[0]
            if codice.startswith("ES"):
                self.__espositori[codice] = Espositore(codice, riga[1], riga[2])
            elif codice.startswith("ST"):
                if len(riga) == 4 or riga[4] == "":
                    self.__stand[codice] = Stand(codice, riga[1], riga[2], riga[3])
                # .isdigit() controlla se il quinto campo è composto da cifre numeriche
                elif riga[4].isdigit():
                    self.__stand[codice] = StandPreseExtra(codice, riga[1], riga[2], riga[3], riga[4])
                else:
                    self.__stand[codice] = StandPremium(codice, riga[1], riga[2], riga[3], riga[4])

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

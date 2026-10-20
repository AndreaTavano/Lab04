class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = int(superficie)
        self.__padiglione = int(padiglione)
        self.__prezzo_base = float(prezzo_base)
        self.__disponibile = True
        self.__espositore = None

    @property
    def codice(self):
        return self.__codice

    @property
    def superficie(self):
        return self.__superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzo_base(self):
        return self.__prezzo_base

    @property
    def disponibile(self):
        return self.__disponibile

    @disponibile.setter
    def disponibile(self, valore):
        self.__disponibile = valore

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self, esp):
        self.__espositore = esp

    @property
    def prezzo(self):
        return self.__prezzo_base

    def __str__(self):
        if self.__disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return f"{self.__codice}: Standard | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo:.2f}€ - {stato}"

class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__numero_prese = int(numero_prese)

    @property
    def prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.__numero_prese)

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - Prese aggiuntive: {self.__numero_prese} - {stato}"

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__posizione = posizione

    @property
    def prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - Posizione: {self.__posizione} - {stato}"
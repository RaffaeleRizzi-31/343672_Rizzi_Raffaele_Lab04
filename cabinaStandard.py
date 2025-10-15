class CabinaStandard:
    def __init__(self,codice, nLetti, ponte, prezzo):
        self._codice = codice
        self._nLetti = nLetti
        self._ponte = ponte
        self._prezzo = prezzo
        self._disponibilita = True
    #-------------------------------------------------
    @property
    def codice(self):
        return self._codice

    @codice.setter
    def codice(self, codice):
        self._codice = codice
    #-------------------------------------------------
    @property
    def disponibilita(self):
        return self._disponibilita
    @disponibilita.setter
    def disponibilita(self, disponibilita):
        self._disponibilita = disponibilita
    #-------------------------------------------------
    @property
    def prezzo(self):
        return self._prezzo
    #-------------------------------------------------
    @property
    def stato(self):
        if self._disponibilita:
            return "Disponibile"
        else:
            return "Non disponibile"
    # -------------------------------------------------
    def __eq__(self, other):
        if not isinstance(other, CabinaStandard):
            return NotImplemented
        return self.codice == other.codice
    def __lt__(self, other):
        if not isinstance(other, CabinaStandard):
            return NotImplemented
        return self.prezzo < other.prezzo
    def __str__(self):
        return f"{self._codice}: Standard | {self._nLetti} letti - Ponte {self._ponte} - Prezzo {self._prezzo:.2f}€ - {self.stato}"
    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(codice= {self._codice}, nLetti= {self._nLetti}, ponte= {self._ponte}, prezzo= {self._prezzo:.2f}, disponibilita= {self._disponibilita}={self.stato})")
class Passeggero:
    def __init__(self, codice, nome, cognome):
        self._codice = codice
        self._nome = nome
        self._cognome = cognome
        self._codiceCabina = None
    #-------------------------------------------------
    @property
    def codice(self):
        return self._codice
    @codice.setter
    def codice(self, codice):
        self._codice = codice
    #-------------------------------------------------
    @property
    def codiceCabina(self):
        return self._codiceCabina
    @codiceCabina.setter
    def codiceCabina(self, codice):
        self._codiceCabina = codice
    #-------------------------------------------------
    def __eq__(self, other):
        if not isinstance(other, Passeggero):
            return NotImplemented
        return self.codice == other.codice
    def __str__(self):
        return f"{self._codice}: {self._nome} {self._cognome}"
    def __repr__(self):
        return (f"{self.__class__.__name__}"
            f"(codice= {self._codice}, nome= {self._nome}, cognome= {self._cognome}, codiceCabina= {self._codiceCabina})")
from cabinaStandard import CabinaStandard

class CabinaDeluxe(CabinaStandard):
    def __init__(self, codice, nLetti, ponte, prezzo, stile):
        super().__init__(codice, nLetti, ponte, prezzo)
        self._stile = stile
        self._prezzoFinale = prezzo*1.20
    #-------------------------------------------------
    @property
    def prezzo(self):
        return self._prezzoFinale
    #-------------------------------------------------
    def __str__(self):
        return f"{self._codice}: Deluxe | {self._nLetti} letti - Ponte {self._ponte} - Prezzo {self._prezzoFinale:.2f}€ - Stile {self._stile} - {self.stato}"
    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(codice= {self._codice}, nLetti= {self._nLetti}, ponte= {self._ponte}, prezzo= {self._prezzoFinale:.2f}, stile= {self._stile}, disponibilita= {self._disponibilita}={self.stato})")
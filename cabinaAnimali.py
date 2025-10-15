from cabinaStandard import CabinaStandard

class CabinaAnimali(CabinaStandard):
    def __init__(self, codice, nLetti, ponte, prezzo, nAnimali):
        super().__init__(codice, nLetti, ponte, prezzo)
        self._nAnimali = nAnimali
        self._prezzoFinale = float(prezzo*(1+0.10*nAnimali))
    #-------------------------------------------------
    @property
    def prezzo(self):
        return self._prezzoFinale
    #-------------------------------------------------
    def __str__(self):
        return f"{self._codice}: Animali | {self._nLetti} letti - Ponte {self._ponte} - Prezzo {self._prezzoFinale:.2f}€ - Max animali {self._nAnimali} - {self.stato}"
    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(codice= {self._codice}, nLetti= {self._nLetti}, ponte= {self._ponte}, prezzo= {self._prezzoFinale:.2f}, nAnimali= {self._nAnimali}, disponibilita= {self._disponibilita}={self.stato})")
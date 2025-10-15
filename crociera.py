from csv import reader
from cabinaStandard import CabinaStandard
from cabinaAnimali import CabinaAnimali
from cabinaDeluxe import CabinaDeluxe
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self._cabine = []
        self._passeggeri = []
    # -------------------------------------------------
    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    # -------------------------------------------------
    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, "r") as infile:
                csvReader = reader(infile)
                for row in csvReader:
                    codice = row[0]
                    if codice[0] == "P":
                        nome, cognome = row[1], row[2]
                        passeggero = Passeggero(codice, nome, cognome)
                        self._passeggeri.append(passeggero)
                    else: # è una cabina
                        nLetti, ponte, prezzo = int(row[1]), int(row[2]), float(row[3])
                        if len(row) == 4: # cabina standard
                            cabina = CabinaStandard(codice, nLetti, ponte, prezzo)
                            self._cabine.append(cabina)
                        elif len(row) == 5:
                            try:
                                nAnimali = int(row[4])
                                numero = True   # è una cabina che ammette animali
                            except ValueError:
                                stile = row[4]
                                numero = False  # è una cabina che deluxe
                            if numero:
                                cabina = CabinaAnimali(codice, nLetti, ponte, prezzo, nAnimali)
                                self._cabine.append(cabina)
                            else:
                                cabina = CabinaDeluxe(codice, nLetti, ponte, prezzo, stile)
                                self._cabine.append(cabina)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' non trovato.")
    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        passeggeroDaCercare = Passeggero(codice_passeggero, "", "")
        passeggeroTrovato = None
        for passeggero in self._passeggeri:
            if passeggero == passeggeroDaCercare:
                passeggeroTrovato = passeggero
                break
        if passeggeroTrovato:
            cabinaDaCercare = CabinaStandard(codice_cabina, 0, 0,0.0)
            cabinaTrovata = None
            for cabina in self._cabine:
                if cabina == cabinaDaCercare:
                    cabinaTrovata = cabina
                    break
            if cabinaTrovata:
                if passeggeroTrovato.codiceCabina == None:
                    if cabinaTrovata.disponibilita == True:
                        passeggeroTrovato.codiceCabina = codice_cabina
                        cabinaTrovata.disponibilita = False
                    else:
                        raise Exception(f"La cabina {codice_cabina} non è disponibile.")
                else:
                    raise Exception(f"Il passeggero {codice_passeggero} ha già una cabina.")
            else:
                raise Exception(f"Cabina {codice_cabina} non trovata.")
        else:
            raise Exception(f"Passeggero {codice_passeggero} non trovato.")
    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self._cabine)
    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for passeggero in self._passeggeri:
            if passeggero.codiceCabina != None:
                print(passeggero,f"| Cabina: {passeggero.codiceCabina}")
            else:
                print(passeggero)
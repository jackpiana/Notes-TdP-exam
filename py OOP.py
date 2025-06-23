from dataclasses import dataclass

"""
esempio creazione classe standard
"""
class Nazione:
    def __init__(self, CCode: int, StateAbb: str, StateNme: str):
        self.CCode = CCode
        self.StateAbb = StateAbb
        self.StateNme = StateNme

    def __eq__(self, other):
        return self.StateAbb == other.StateAbb

    def __hash__(self):
        return hash(self.StateAbb)

    def __repr__(self):
        return (f"Country(CCode={self.CCode}, StateAbb='{self.StateAbb}', "
            f"StateNme='{self.StateNme}'")

    def __str__(self):
        return f"{self.StateAbb} - {self.StateNme}"

    def __lt__(self, other):
        return self.StateNme.lower() < other.StateNme.lower()

    """
    Il metodo __hash__ in Python definisce come un oggetto deve 
    essere convertito in un valore intero univoco (hash), 
    utilizzato principalmente in:
    Dizionari: Per identificare le chiavi in modo efficiente.
    Set: Per determinare l'unicità degli elementi.
    
    NB
    
    __hash__ deve essere basato sugli stessi attributi usati in __eq__.
    Define __eq__() and __hash__() using the exact set of fields that
    compose the primary key of the table
    """

    """ __repr__
     genera una stringa che rappresenta l'oggetto """

    """ __eq__
    Definisce l'uguaglianza tra oggetti Country basata sul codice paese (StateAbb) case-insensitive
    Viene usato automaticamente da: ==, !=, set, dizionari, list.count(), list.index(), in, 
    unittest.assertEqual(), pandas.DataFrame.equals() e altre operazioni di confronto
    Args:
    other (Any): Oggetto da confrontare, preferibilmente Country
    Returns:
    bool: True se gli StateAbb sono equivalenti (ignorando maiuscole/minuscole)
    False se other non è un Country o se il confronto fallisce
    Note:
    Per mantenere il contratto hash-eq, sovrascrivere anche __hash__ quando si ridefinisce __eq__
    """

    """ __lt__
    Permette il confronto tra due oggetti Country basato sul nome del paese (case insensitive)
    Viene usato automaticamente da: sorted(), list.sort(), min(), max()
    Args:
        other (Country): Altro oggetto Country da confrontare
    Returns:
        bool: True se questo paese viene prima alfabeticamente
    """

    """ __str__
    Restituisce una rappresentazione leggibile e user-friendly dell'oggetto Country.
    Viene usato automaticamente da: print(), str(), f-string, formattazione stringhe.
    Differisce da __repr__ che è più tecnico e usato per debugging.
    """


""""
Esempio di classe creata con @dataclass

@dataclass automatizza la creazione di classi che sono principalmente contenitori di dati

Cosa viene generato automaticamente?
__init__()	Sempre	Inizializza tutti gli attributi dichiarati.
__repr__()	Sempre	Rappresentazione stringa con nome classe e attributi.
__eq__()	Sempre	Confronta tutti gli attributi per uguaglianza.
__hash__()	Se frozen=True	Calcola l'hash basato sugli attributi immutabili.
__lt__()    Se order=True	Confronta gli attributi nell'ordine dichiarato.
"""
@dataclass
class Country:
    CCode: int
    StateAbb: str
    StateNme: str

    def __eq__(self, other):
        return self.StateAbb == other.StateAbb

    def __hash__(self):
        return hash(self.StateAbb)

    def __str__(self):
        return f"{self.StateAbb} - {self.StateNme}"

    def __lt__(self, other):
        return self.StateNme.lower() < other.StateNme.lower()

"""
order=True (Ordinamento)
Cosa fa:
Genera automaticamente i metodi di confronto (__lt__, __le__, __gt__, __ge__),
ordinando gli oggetti in base all'ordine di dichiarazione dei campi.
"""
@dataclass(order=True, frozen=True)
class Country:
    CCode: int
    StateAbb: str
    StateNme: str

"""
isinstance(oggetto, classe)  # Restituisce True o False
"""

import networkx as nx

class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def build_graph(self):
        self.grafo.clear()

    """
    RICORSIONE
    template funzioni 
    """
    def calcola_bestpath(self):
        pass

    def ricorsione(self, parziale):
        rimanenti = self.calcola_rimanenti(parziale)
        if rimanenti == []:
            self.calcolaPunteggio(parziale)
        else:
            rimanenti = rimanenti.copy()
            for n in rimanenti:
                parziale.append(n)
                parziale = parziale.copy()
                self.ricorsione(parziale)
                parziale.pop()

    def calcola_rimanenti(self, parziale):
        return rimanenti

    def calcolaPunteggio(self, parziale):
        pass

    def isAmmissibile(self):
        pass






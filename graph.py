import networkx as nx

#template funzione controller
def handle_creaGrafo(self, e):
    self._view.lv_result.controls.clear()
    self._view.update_page()
    self.read_casellaTesto_intero()

    self._model.build_graph(self.numCompagnie)

    self._view.lv_result.controls.append(ft.Text(self._model.grafo))

    self._view.update_page()



"""
NODES can be any hashable object

EDGES are tuples with optional edge data (stored in dictionary)
grafo.edges(data=True) restituisce lista di tuple del tipo:
(nodoA, nodoB, {'weight': 3.5, 'color':'red'}) 
"""

graph = nx.Graph()
diGraph = nx.DiGraph()
multiGraph = nx.MultiGraph()
multiDiGraph = nx.MultiDiGraph()

"""
Quando aggiungi archi (edges) a un grafo in NetworkX 
senza aver prima aggiunto esplicitamente i nodi (nodes) collegati
da quegli archi, NetworkX aggiunge automaticamente i nodi mancanti al grafo.
"""
graph.add_node("A")
graph.add_edge("A", "B")

graph.add_nodes_from(list_nodes)
graph.add_edges_from(list_edges)
elist = [(1, 2, 1), (2, 3, 1), (1, 4, 1), (4, 2, 1),
         ('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
g.add_weighted_edges_from(elist)

peso = m.grafo[nodo1][nodo2]['weight']
print(d1, d2, peso) #per printare il valore di edge


#numero nodi e archi
ft.Text(f"{self._model.grafo}") #it prints graph with n nodes and e edges
numero_nodi = graph.number_of_nodes(), len(graph.nodes)
numero_edges = graph.number_of_edges(), len(graph.edges)

#GETTER nodi e archi
G.edges(nodo) #Restituisce tutti gli archi collegati al nodo.

G.nodes() #Restituisce tutti i nodi POTREBBE DARE PROBLEMI
G.edges() #Restituisce tutti gli archi POTREBBE DARE PROBLEMI
list(self.grafo.nodes)
list(self.grafo.edges)

#NEIGHBOORS
neighbors = list(self._graph.neighbors(n)) #Restituisce una lista di nodi adiacenti (direttamente connessi) al nodo n

succesori = grafo.successors(nodo_sorgente) # nodi direttamente connessi tramite un arco uscente da un nodo specifico n in un grafo orientato (DiGraph) di NetworkX
predecessori=  grafo.predecessors(nodo_sorgente) #complementare

list(grafo.edges(nodo, data=True)) #lista di tutti gli archi collegati a un nodo specifico
list(grafo.out_edges(nodo, data=True)) #tutti gli archi uscenti da un nodo specifico
list(grafo.in_edges(nodo, data=True) #tutti gli archi entranti in un nodo specifico

#degree
graph.degree[node]
graph.in_degree[node]
graph.out_degree[node]

"""
COMPONENTI CONNESSE
In un grafo non orientato, una componente connessa è 
un insieme di nodi in cui esiste un percorso tra ogni coppia di nodi.
"""
nx.number_connected_components(G) # Restituisce il numero di componenti connesse.
nx.node_connected_component(G, node) # restituisce Un set contenente tutti i nodi
                                    # che fanno parte della componente connessa
                                    #a cui appartiene il nodo specificato
nx.connected_components(G)	#Lista di componenti connesse.


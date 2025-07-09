import networkx as nx

    """
    NODES can be any hashable object
    
    EDGES are tuples with optional edge data (stored in dictionary)
    grafo.edges(data=True) restituisce lista di tuple del tipo:
    (nodoA, nodoB, {'weight': 3.5, 'color':'red'}) 
    """

    graph = nx.Graph()                  #orientamento: no       archi multipli: no
    diGraph = nx.DiGraph()              #orientamento: si       archi multipli: no
    multiGraph = nx.MultiGraph()        #orientamento: no       archi multipli: si
    multiDiGraph = nx.MultiDiGraph()    #orientamento: si       archi multipli: si

    """
    Quando aggiungi archi (edges) a un grafo in NetworkX 
    senza aver prima aggiunto esplicitamente i nodi (nodes) collegati
    da quegli archi, NetworkX aggiunge automaticamente i nodi mancanti al grafo.
    """
    self.grafo.add_node("A")
    self.grafo.add_edge("A", "B")

    self.grafo.add_nodes_from(list_nodes)
    self.grafo.add_edges_from(list_edges)


    # Aggiungi un arco con attributo 'weight'
    self.grafo.add_edge(1, 2, weight=4.5)
    self.grafo.add_edge(2, 3, weight=2.1)

    # Puoi anche usare un dizionario per gli attributi
    G.add_edge(3, 4, **{'weight': 7.2, 'color': 'blue'})

    elist = [(1, 2, 1), (2, 3, 1), (1, 4, 1), (4, 2, 1),
             ('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
    self.grafo.add_weighted_edges_from(elist)


    self.grafo.add_edge(5, 6)  # Arco senza peso iniziale
    self.grafo.edges[5, 6]['weight'] = 3.8  # Aggiungi/modifica peso dopo

    peso = self.grafo[nodo1][nodo2]['weight']
    peso = self.grafo.get_edge_data(1, 2)['weight']

    print(d1, d2, peso) #per printare il valore di edge

    """
    GETTING values
    """
    #numero nodi e archi
    ft.Text(f"{self._model.grafo}") #it prints graph with n nodes and e edges
    numero_nodi = graph.number_of_nodes(), len(graph.nodes)
    numero_edges = graph.number_of_edges(), len(graph.edges)

    #GETTER nodi e archi
    self.grafo.edges(nodo) #Restituisce tutti gli archi collegati al nodo.

    list(self.grafo.nodes)
    list(self.grafo.edges)            #returns tupla con (n1, n2)
    list(self.grafo.edges(data=True)) #returns tupla con (n1, n2, dizAttributi)


    #NEIGHBOORS
    neighbors = list(self.grafo.neighbors(n)) #Restituisce una lista di nodi adiacenti (direttamente connessi) al nodo n

    succesori = self.grafo.successors(nodo_sorgente)        #nodi direttamente connessi tramite un arco uscente da un nodo specifico n in un grafo orientato (DiGraph) di NetworkX
    predecessori=  self.grafo.predecessors(nodo_sorgente)   #complementare

    list(self.grafo.edges(nodo, data=True))      #lista di tutti gli archi collegati a un nodo specifico
    list(self.grafo.out_edges(nodo, data=True))  #tutti gli archi uscenti da un nodo specifico
    list(self.grafo.in_edges(nodo, data=True)    #tutti gli archi entranti in un nodo specifico

    """
    DEGREE
    """
    self.grafo.degree[node]
    self.grafo.in_degree[node]
    self.grafo.out_degree[node]

    """
    COMPONENTI CONNESSE
    In un grafo non orientato, una componente connessa è 
    un insieme di nodi in cui esiste un percorso tra ogni coppia di nodi.
    """
    nx.number_connected_components(self.grafo) # Restituisce il numero di componenti connesse.
    nx.node_connected_component(self.grafo, node) # restituisce Un set contenente tutti i nodi
                                        # che fanno parte della componente connessa
                                        #a cui appartiene il nodo specificato
    nx.connected_components(self.grafo)	#returns generatore di set di componenti connesse su cui iterare


    """
    SHORTEST PATH
    """
    nx.shortest_path(self.grafo, source, target)   #Restituisce la lista dei nodi del cammino più corto.

    nx.dijkstra_path(G, source, target, weight='weight')
    """
    :return: lista di nodi che rappresenta 
    il percorso minimo da source a target 
    che minimizza il peso degli archi.
    """

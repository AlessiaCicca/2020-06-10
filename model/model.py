import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.generi=DAO.getGeneri()
        self.grafo = nx.Graph()
        self._idMap = {}
        self._idMapStringa= {}

    def creaGrafo(self, genere):
        self.nodi = DAO.getNodi(genere)
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[v.id] = v
        for v in self.nodi:
            self._idMapStringa[f"{v.last_name},{v.first_name} ({v.id})"] = v
        self.addEdges(genere)
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self, genere):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni(genere)
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:

                    self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)
    def analisi(self,attoreStringa):
        raggiungibili=[]
        attore=self._idMapStringa[attoreStringa]
        for nodi in nx.dfs_tree(self.grafo, attore):
            raggiungibili.append((nodi, nodi.last_name))
        return sorted(raggiungibili, key=lambda x:x[1])



"""PESO MAGGIORE :
Stampare i 5 archi di peso maggiore, ordinati in ordine decrescente di peso (vedere esempi di soluzione). Per
ognuno di questi 5 archi stampare l’id del nodo di origine, l’id del nodo di destinazione, ed il peso

IN MODEL :"""
def get_top_edges(self):
            sorted_edges = sorted(self._grafo.edges(data=True), key=lambda edge: edge[2].get('weight'), reverse=True)
            return sorted_edges[0:5]

"""IN CONTROLLER: 
top_edges = self._model.get_top_edges()
                for edge in top_edges:
                    self._view.txt_result1.controls.append(ft.Text(f"{edge[0].id} -> {edge[1].id} | weight = {edge[2]['weight']}"))"""


"""USCENTI I 5 nodi col maggiore numero di archi uscenti col numero di archi uscenti ed il peso complessivo di
questi archi (la somma dei loro pesi):"""
def get_node_max_uscenti(self):
        sorted_nodes = sorted(self._graph.nodes(), key=lambda n: self._graph.out_degree(n), reverse=True)
        result = []
        for i in range(min(len(sorted_nodes), 5)):
            peso_tot = 0.0
            for e in self._graph.out_edges(sorted_nodes[i], data=True):
                peso_tot += float(e[2].get("weight"))
            result.append((sorted_nodes[i], self._graph.out_degree(sorted_nodes[i]), peso_tot))
        return result
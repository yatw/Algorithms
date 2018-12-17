class Graph:
    'Common base class for all graph objects'
    
    def __init__(self, direct=None, weight=None, vertices=None, edges=None):


        self.directed = False # default undirected
        if (direct):
            self.directed = True

        self.weighted = False # default unweighted
        if (weight):
            self.weighted = True

        self.vertices = set()
        if (vertices is not None):
            self.vertices = vertices
            
        self.edges = set()
        if (edges is not None):
            self.edges = edges


        self.label = {} # for connected component labeling
        # {node:label}

        

    def Set_directed(self, d):
        # boolean d indicated directed graph or not

        if d:
            self.directed = True

    def Set_weighted(self, w):
        # boolean w indicated weighted graph or not

        if w:
            self.weighted = True        

    def Set_edges(self, edges):
        self.edges = edges

    def Set_vertices(self, vertices):
        self.vertices = vertices

    def Add_vertice(self, v):
        self.vertices.add(v)

    def Add_edge(self, u, v, w = 0):
        # u is start, v is destination

        self.Add_vertice(u)
        self.Add_vertice(v)
        
        if self.directed:
            self.edges.add(tuple((u,v,w)))

        else: # if undirected, edge can go both way
            self.edges.add(tuple((u,v,w)))
            self.edges.add(tuple((v,u,w)))

    def FindParent(self, discovery_edges, v):
        '''Mainly for Biconnected Component Algorithm,
           Given the DFS discovery edges, and node
           return parent node
        '''

        for p,d in discovery_edges:

            if d == v:
                return p

        print("No node can reach ", v)
        return None
        

    def GetIncidentEdges(self, v):
        ''' Return all out going edges from vertex '''

        IncidentEdges = []
        for s,d,w in self.edges:
            if s == v:
                IncidentEdges.append(tuple((s,d)))
            
        return IncidentEdges

    def GetDestination(self,edge,v):
        '''Given edge {v,d}, return d'''

        if v != edge[0]:
            return edge[0]
        
        return edge[1]


if __name__ == "__main__":

    G1 = Graph()
    G2 = Graph()
    G1.Add_vertice('A')


    print(G2.vertices)





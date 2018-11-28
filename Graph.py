class Graph:
    'Common base class for all graph objects'

    vertices = [] #nodes
    edges = []  # edges store as tuple of 2 vertices
    
    label = {}  # mainly for Connected Component Labeling
                # dictionary storing {vertex: label}

    linked = [] # mainly for Biconnected Component Algorithm
                # nodes that are in it are linked
    
    def __init__(self, vertices=[], edges=[], label={}, linked = []):
        self.vertices = vertices
        self.edges = edges
        self.label = label
        self.linked = linked

    def Initalize_edges(self, edges):
        self.edges = edges

    def Initalize_vertices(self, vertices):
        self.vertices = vertices

    def Add_vertex(self, v):
        self.vertices.append(v)

    def Add_edge(self, e):
        self.edges.append(e)

    def FindParents(self, v):
        '''Go through all edges and return the vertexs that could go to v'''

        possible_parents = []
        for e in self.edges:

            if v in e:
                p = self.GetDestination(e,v)
                if p not in possible_parents:
                    possible_parents.append(p)
        return possible_parents
        

    def GetIncidentEdges(self, v):
        ''' Return all out going edges from vertex '''

        IncidentEdges = []
        for o,d in self.edges:
            if (v == o or v == d):
                IncidentEdges.append(tuple((o,d)))
            
        return IncidentEdges

    def GetDestination(self,edge,v):
        '''Given edge {v,d}, return d'''

        if v != edge[0]:
            return edge[0]
        
        return edge[1]
     

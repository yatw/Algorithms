class Graph:
    'Common base class for all graph objects'

    vertices = [] #nodes
    edges = []  # edges store as set of 2 vertices
    
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        

    def GetIncidentEdges(self, v):
        ''' Incident edges are the edge that connect to this vertice '''

        IncidentEdges = []
        for o,d in self.edges:
            if (v == o or v == d):
                IncidentEdges.append({o,d})
            
        return IncidentEdges

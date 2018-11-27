class Graph:
    'Common base class for all graph objects'

    vertices = [] #nodes
    edges = []  # edges store as set of 2 vertices
    label = {}  # dictionary store the vertex and label
    
    def __init__(self, vertices, edges, label={}):
        self.vertices = vertices
        self.edges = edges
        self.label = label


    def GetIncidentEdges(self, v):
        ''' Incident edges are the edge that connect to this vertice '''

        IncidentEdges = []
        for o,d in self.edges:
            if (v == o or v == d):
                IncidentEdges.append({o,d})
            
        return IncidentEdges

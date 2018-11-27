class Graph:
    'Common base class for all graph objects'

    vertices = [] #nodes
    edges = []  # edges store as pair of 2 vertices
    
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

                for i in e:
                    if v != i:
                        possible_parents.append(i)
                
        return possible_parents
        

    def GetIncidentEdges(self, v):
        ''' Return all edges connect to this vertex '''

        IncidentEdges = []
        for o,d in self.edges:
            if (v == o or v == d):
                IncidentEdges.append({o,d})
            
        return IncidentEdges

    def GetDestination(edge,v):
        '''Given edge {v,d}, return d'''

        tuple(edge)
        for node in edge:
            if node != v:
                return node

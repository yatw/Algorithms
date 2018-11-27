from PIL import Image
from Graph import Graph


def getDestination(edge,origin):

    for vertices in edge:
        if (vertices != origin):
            return vertices

        
def ConnectedComponentLabeling(G):
    '''Assign a label to vertices such that vertices with same label are
       indicated to be in the same connected component'''

    label = 0 
    all_vertices = G.vertices
    for v in all_vertices:
        if v not in G.label: # this vertex has no label
            label += 1
            DSFLabel(G,v,label)
            

    return None

def DSFLabel(G,v,label, explored_e = []):
    '''Apply Depth First Search Algorithm and label visited vertice'''

    
    G.label[v] = label # store that labeling in the graph class
    ce = G.GetIncidentEdges(v)
    for e in ce:
        if e not in explored_e:
            
            next_vertex = getDestination(e,v)
            explored_e.append(e)
        
            if (next_vertex not in G.label):
                DSFLabel(G,next_vertex,label)
    
    return None

    
image = Image.open('CCLGraph.PNG').show()



V = ['A','B','C','D','E','F']
E = [{'A','B'},{'A','C'},{'B','C'},{'C','D'},{'E','F'}]
G = Graph(V,E)

ConnectedComponentLabeling(G)
print(G.label)

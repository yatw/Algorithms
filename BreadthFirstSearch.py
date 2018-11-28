from PIL import Image
from Graph import Graph


    
def BFS(G,S):
    '''Perform Breadth First Search on the graph, keep track of
       discovery edges and cross edges
    '''
    all_levels = [] #keep track of level with index 
    
    this_level = [S] #initalize with starting vertice
    next_level = []
    visited_nodes = [S]  
    discovery_edges = []
    cross_edges = []

    while len(this_level) != 0:
        
        for n in this_level:
            #print(n)
            ce = G.GetIncidentEdges(n) # connected edges
            
            for edge in ce:
                #print("-",edge)
                if edge not in discovery_edges:
                    
                    destination = G.GetDestination(edge, n)
                    #print('-', destination)
                    if destination not in visited_nodes:

                        discovery_edges.append(edge)
                        next_level.append(destination)
                        visited_nodes.append(destination)
                                             
                    else:
                        if edge not in cross_edges:
                            cross_edges.append(edge)

        all_levels.append(this_level)
        this_level = next_level
        next_level = []
    #print(discovery_edges)
    #print(cross_edges)
    return all_levels


if __name__ == "__main__":
    
    #image = Image.open('images\BFSGraph.PNG').show()




    V = ['A','B','C','D','E','F','G','H','I','J','K']
    E = [('A','B'),('A','C'),('A','D'),('A','E'),('C','D'),('D','E'),
         ('B','F'),('C','G'),('G','F'),('F','J'),('G','H'),('G','J'),
         ('J','K'),('H','I'),('H','K')]   
    G = Graph(V,E)


    r = BFS(G,'A')
    for i in r:
        print(i)


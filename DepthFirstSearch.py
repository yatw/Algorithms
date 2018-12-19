from PIL import Image
from Graph import Graph



def DFS(G,S,explored_v = None ,explored_e = None,back_edge = None, sort = None):
    '''Perform Depth First Search on the graph, record back edge at the same time

    S = starting vertice
    explored_v = keep track of the vertice we visited in order
    explored_e = both discovery edge and back edge that we visited
    back_edge = new edge that go back to a visited vertex
    '''

    if explored_v is None:
        explored_v = []
    if explored_e is None:
        explored_e = []
    if back_edge is None:
        back_edge = []
    if sort is None:
        sort = False


    #print(explored_e)
    explored_v.append(S)
    
    ce = G.GetIncidentEdges(S) #get all the edges connecting to S
   
    if sort:
        # sort option remove reandomness when picking discovery edge
        # will instead take in Alphabetical order
        ce = sorted(ce, key = lambda x: x[1])
    #print(ce)
    for u,v in ce: # for all the connecting edges
        
        if tuple((u,v)) not in explored_e and tuple((v,u)) not in explored_e :
            # this is not the path you come from
     
            destination = G.GetDestination(tuple((u,v)), S)
            explored_e.append(tuple((u,v))) 
                        
            if destination not in explored_v:
                # and never explored the destination vertice
                # # gonna explore down this path!

                #print("go for destination " + destination)
                DFS(G,destination,explored_v,explored_e,back_edge, sort)
                #print("back to "+S)
                #print("Available edges: ") # edges not explored before
                #print([p for p in ce if p not in explored_e])
                

            else:
                # if it is a new path that goes to a visted vertice,
                # this edge is a back_edge
                back_edge.append(tuple((u,v)))
    
       
    return explored_v, explored_e, back_edge


if __name__ == "__main__":
    # This example produce different result randomly because of the
    # set implementation of the edges
    # which discovery edge to take depends on
    # which edge got run first in the forloop

    # what the example graph looks like
    image = Image.open('images\DFSGraph.PNG').show()


    V = ['A','B','C','D','E','F','G','H','I','J','K']
    E = [('A','B'),('A','C'),('A','D'),('A','E'),('C','D'),('D','E'),
         ('B','F'),('C','G'),('G','F'),('F','J'),('G','H'),('G','J'),
         ('J','K'),('H','I'),('H','K')]
    G = Graph()
    G.set_directed = False
    G.set_weighted = False

    for u,v in E:
        G.Add_edge(u,v)


    path,_,be = DFS(G,'A', sort = True)
    print("One possible DFS result:")
    print(path)
    print("Back edges")
    print(be)


    G_r = G.Reverse_edges()
    path,_,be = DFS(G_r,'A', sort = True)
    

     


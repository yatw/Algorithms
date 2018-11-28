from PIL import Image
from Graph import Graph


def DFS(G,S,explored_v =[],explored_e =[],back_edge =[]):
    '''Perform Depth First Search on the graph, record back edge at the same time

    S = starting vertice
    explored_v = keep track of the vertice we visited in order
    explored_e = both discovery edge and back edge that we visited
    back_edge = new edge that go back to a visited vertex
    '''

    explored_v.append(S)
    
    ce = G.GetIncidentEdges(S) #get all the edges connecting to S


    for e in ce: # for all the connecting edges
        
        if e not in explored_e:
            # this is not the path you come from
     
            destination = G.GetDestination(e, S)
            explored_e.append(e)
                        
            if destination not in explored_v:
                # and never explored the destination vertice
                # go for it!
                #print("go for destination " + destination)
                DFS(G,destination,explored_v,explored_e,back_edge)
                #print("back to "+S)
                #print("Available edges: ") # edges not explored before
                #print([p for p in ce if p not in explored_e])
                

            else:
                # if it is a new path that goes to a visted vertice,
                # this edge is a back_edge
                back_edge.append(e)
    
       
    return explored_v, explored_e, back_edge


if __name__ == "__main__":

    image = Image.open('images\DFSGraph.PNG').show()


    V = ['A','B','C','D','E','F','G','H','I','J','K']
    E = [('A','B'),('A','C'),('A','D'),('A','E'),('C','D'),('D','E'),
         ('B','F'),('C','G'),('G','F'),('F','J'),('G','H'),('G','J'),
         ('J','K'),('H','I'),('H','K')]
    G = Graph(V,E)


    path,_,_ = DFS(G,'A')
    print(path)


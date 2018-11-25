from PIL import Image
from Graph import Graph


def getDestination(edge,origin):

    for vertices in edge:
        if (vertices != origin):
            return vertices

    
def DFS(G,S,explored_v =[],explored_e =[],back_edge =[]):
    '''Perform Depth First Search on the graph, record back edge at the same time

    S = starting vertice
    explored_v = keep track of the vertice we visited
                 it is also the order we traversed the vertices
    explored_e = keep track of edges we explored
    back_edge = keep track of edges that go back to visited vertices
    '''

    explored_v.append(S)
    
    ce = G.GetIncidentEdges(S) #get all the edges connecting to S

    

    for e in ce: # for all the connecting edges
        
        if e not in explored_e:
            # never explored this edge before
     
            destination = getDestination(e, S)
            explored_e.append(e)
                        
            if destination not in explored_v:
                # and never explored the destination vertice
                # go for it!
                print("go for destination " + destination)
                DFS(G,destination,explored_v,explored_e,back_edge)
                print("back to "+S)
                print("Available edges: ") # edges not explored before
                print([p for p in ce if p not in explored_e])
                

            else:
                # if it goes back to a visted vertice, this edge is a back_edge
                back_edge.append(e)
    
       
    return explored_v

image = Image.open('DFSGraph.PNG').show()




V = ['A','B','C','D','E','F','G','H','I','J','K']
E = [{'A','B'},{'A','C'},{'A','D'},{'A','E'},{'C','D'},{'D','E'},{'B','F'},{'C','G'},{'G','F'},{'F','J'},{'G','H'},{'G','J'},{'J','K'},{'H','I'},{'H','K'}]
G = Graph(V,E)


r = DFS(G,'A')
print(r)


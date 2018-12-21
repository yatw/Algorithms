from PIL import Image
from Graph import Graph
import math



def BellmanFord(G,S):
    '''BellmanFord examines all out going edges for every vertex,
       and repeats this iteration for n-1 times,
       n-1 because no simple path can have more than n-1 edges
       this guarteen to have shortest distance after n-1 iterations

       If negative cycle exist, there is no shortest path
    '''

    # initalize result table with all the vertices
    # and set their shortest distance to infinity
    result = {}
    for v in G.vertices:
        result[v] = math.inf # {vertex: distance}

    # starting vertex distance to itself is 0
    result[S] = 0

    for i in range(1,len(G.vertices)): #BellmanFord iterations is vertices -1

        #print(i)
        for u,v,w in G.edges:
            #print(u,v,w)
            if u in result:
                
                if result[u] + w < result[v]:
                    result[v] = result[u] + w
            #print(result)


    #Check for negative cycle, 
    for u,v,w in G.edges:
        if (result[u] + w < result[v]):
            # If you can still find improvement after n-1 cycle
            # that means the graph contain negative cycle
            # because you can only find improvement with n cycle
            # when you repeated a vertex
            print("G  contains a negative-weight cycle")
        #return "G contains a negative-weight cycle"

    return result 
        

if __name__ == "__main__":

    image = Image.open('images/bellmanfort_example.PNG').show()
    
    V = ['A','B','C','D','E','F']
    E = [('A','B',3),('B','C',3),('C','D',3),('D','F',-3 ),('A','D',10),
         ('A','E',2),('E','F',6)]

    E2 = [('A','B',2),('B','C',-6),('C','A',3)]
         

    G = Graph()
    G.Set_directed(True)
    G.Set_weighted(True)

    for u,v,w in E:
        G.Add_edge(u,v,w)

    result = BellmanFord(G,'A')
    for r in result:
        print(r, result[r])


           

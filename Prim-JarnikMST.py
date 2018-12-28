from PIL import Image
from Graph import Graph
import math


'''
Same with Dijkstra Prim-Jarnik don't guarteen to work with negative wegight because
once it done visiting a node, it will consider it done.

This miss potnetially big weighted that get cancel out by a negative weight.


Very Similar to Dijkstra by picking the out going edge with the lowest cost
to connect, the only difference is it does not record the total distance from
the starting vertex, only the distance from the cloest vertex in the tree
'''


def Prim_Jarnik(G,S):
    '''Prim-Jarnik MST Algorithm return the connection to all vertices
       that give the lowest cost (form a minimum spanning tree)
    '''

    # initalize result table with all the vertices
    # and set their distance to infinity, parents all None
    result = {}
    for v in G.vertices:
        result[v] = [math.inf, None] # {vertex: [distance, parent]}

    # starting vertex distance to itself is 0
    result[S][0] = 0


    visited_vertices = []

    while (len(visited_vertices) < G.Vertices_count()):

        # pick the outgoing edge with smallest distance to start explore
        # I use a forloop approach here, but a priority heap would be better
        vertex_smallest_cost = None
        smallest_cost = math.inf
        for v in sorted(result):

            if v not in visited_vertices:
                if result[v][0] < smallest_cost:
                    vertex_smallest_cost = v
                    smallest_cost = result[v][0]

        
        can_reach = G.GetIncidentEdges(vertex_smallest_cost)

        for u,v,w in can_reach:
            if v not in visited_vertices:

                if (w < result[v][0]):
                    result[v][0] = w
                    result[v][1] = u

        visited_vertices.append(vertex_smallest_cost)

    return result


        

if __name__ == "__main__":

    image = Image.open('images\prim-Jarnik-example.PNG').show()
    
    V = ['A','B','C','D','E','F','G','H','I','J','K']
    E = [('D','C',5),('D','E',7),('C','H',12),('H','E',6),('C','B',6),
         ('H','G',4),('E','F',5),('B','G',3),('G','F',2),('B','A',8),
         ('A','F',9),('A','I',19),
         ('I','J',14),('I','K',12),('J','K',9)]
         

    G = Graph()
    G.Set_directed(False)
    G.Set_weighted(True)

    for u,v,w in E:
        G.Add_edge(u,v,w)

    result = Prim_Jarnik(G,'H')
    for i in sorted(result):
        print(i, result[i])

           

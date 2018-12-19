from PIL import Image
from Graph import Graph
import math


'''
The reason Dijkstra don't guarteen to work with negative wegight is because
once it done visiting a node, it will consider it done.

This miss potnetially big weighted that get cancel out by a negative weight.
'''


def Dijkstra(G,S):
    '''Disjkstra's shortest path algorithm calculate the information
       of shortest path and cost to all vertices from starting vertex
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

                new_cost = result[u][0] + w
                if (new_cost < result[v][0]):
                    result[v][0] = new_cost
                    result[v][1] = u

        visited_vertices.append(vertex_smallest_cost)

    return result


        

if __name__ == "__main__":

    image = Image.open('images\dijkstra_example.PNG').show()
    
    V = ['A','B','C','D','E','F','G','H','I','J']
    E = [('A','B',12),('A','C',3),('A','D',7),('B','C',8),('C','D',6),
         ('B','E',15),('C','F',2),('D','G',1),('C','E',5),('C','G',4),
         ('E','F',5),('F','G',6),
         ('E','I',10),('G','J',9),('F','H',10),('E','H',9),('G','H',6),
         ('H','I',2),('H','J',5),('I','J',12)]
         

    G = Graph()
    G.Set_directed(False)
    G.Set_weighted(True)

    for u,v,w in E:
        G.Add_edge(u,v,w)

    result = Dijkstra(G,'A')
    for i in sorted(result):
        print(i, result[i])

           

from PIL import Image
from Graph import Graph
from DepthFirstSearch import DFS

'''
Pick a start vertex in G
run DFS in G, if some vertex is not reachable, report NO
reverse all edges in G
run DFS in G _reverse, if some vertex is not reachable, report NO

report YES
runs in O(m+n) time
'''

def TestStrongConnectivity(G,V):

    
    explored_v, explored_e, back_edge = DFS(G,V)

    
    if len(explored_v) != G.Vertices_count():
        return "NOT Strongly connected"

    print(explored_v)
    G_r = G.Reverse_edges()
    explored_v, explored_e, back_edge = DFS(G_r,V)

    print(explored_v)
    if len(explored_v) != G.Vertices_count():
        return "NOT Strongly connected"



    return "Strongly connected"

if __name__ == "__main__":

    image = Image.open('images\StrongConnectivity.PNG').show()
    
    G1 = Graph()
    G1.Set_weighted(False)
    G1.Set_directed(True)

    V1 = ['A','B','C','D','E']
    E1 = [('A','B'),('B','C'),('C','A'),('E','A'),('B','D'),
         ('C','D'),('D','E'),]

    for u,v in E1:
        G1.Add_edge(u,v)
        
    print("G1", TestStrongConnectivity(G1,'A'))


    G2 = Graph()
    G2.Set_weighted(False)
    G2.Set_directed(True)

    V2 = ['A','B','C','D','E']
    E2 = [('A','B'),('B','C'),('C','A'),('A','E'),('B','D'),
         ('C','D'),('D','E'),]

    for u,v in E2:
        G2.Add_edge(u,v)
        
    print("G2",
          TestStrongConnectivity(G2,'A'))




    

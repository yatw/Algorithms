from PIL import Image
from Graph import Graph

def TopologicalSort(G):
    '''
        Start with vertex that has no indegree (no prequisite)
        continue to take out vertex. If no vertex with in degree 0
        exist, this graph contain cycle
    '''

    total_vertices = len(G.vertices)

    TopologicalOrder = {}
    order = 1  

    Indegree_table = {}


    while(len(TopologicalOrder) != total_vertices):
        
        vertex_with_no_indegree = None

        for v in G.vertices:
            indegree = G.Indegree(v)
            Indegree_table[v] = indegree

            if (indegree == 0) and v not in TopologicalOrder:
                vertex_with_no_indegree = v
                
        print(Indegree_table)
        if vertex_with_no_indegree is None:
            return "Contain cycle, not a DAG"
        
        print("Remove vertex", vertex_with_no_indegree)
        G.Remove_vertex(vertex_with_no_indegree)

        for v in G.vertices:
            Indegree_table[v] = G.Indegree(v)

        TopologicalOrder[vertex_with_no_indegree] = order
        order+= 1
        
    return TopologicalOrder




if __name__ == "__main__":

    G = Graph()
    G.Set_weighted(False)
    G.Set_directed(True)

    V = ['A','B','C','D','E','F','H']
    E = [('H','F'),('H','A'),('H','B'),('B','A'),('B','C'),('F','E'),
         ('A','F'),('A','E'),('C','A'),('D','E'),('D','A'),('D','C')]

    for u,v in E:
        G.Add_edge(u,v)


    image = Image.open(r"images\topological.png").show()
    order = TopologicalSort(G)
    for i in sorted(order):
        print(i, order[i])




        

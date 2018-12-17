from PIL import Image
from Graph import Graph
from DepthFirstSearch import DFS


def Bicomponent(G,S):
    '''Construct an auxiliary graph that shows biconnected component'''

    Auxiliary = Graph()  # initially empty auxiliary graph
   
    Auxiliary.Set_directed(True)
    Auxiliary.Set_weighted(False)
    
    explored_v, explored_e, back_edges = DFS(G,S, sort = True) # run DFS once
    discovery_edges = [p for p in explored_e if p not in back_edges]
    examined_backedges = []
    print("---------------------------------------------------")
    print("Above is DFS information")
    # add all discovery edges as vertices

    for u,v in discovery_edges:
        Auxiliary.Add_vertice(tuple((u,v)))

    print(Auxiliary.vertices)
    # for every node, DFS reach order, process back edges that link to it
    for v in explored_v: 
        
        for be in back_edges:
            
            if v in be and be not in examined_backedges:
                print("Back Edge", be, "connect to vertice", v)
                
                examined_backedges.append(be)
                Auxiliary.Add_vertice(be)

                u = G.GetDestination(be,v)

                while (u != v):
                    
                    p = G.FindParent(discovery_edges, u)
              
                    f = tuple((p,u))
                    
                    Auxiliary.Add_edge(be,f)
                    print("Added", be, "link to", f)
                    u = p

              
                
    return Auxiliary

if __name__ == "__main__":

    image = Image.open('images\AuxiliaryGraph.PNG').show()
    V = ['A','B','C','D','E','F','H','J','K','L','M','P','N','Q']
    E = [('A','B'),('A','C'),('B','C'),('C','D'),('D','E'),('E','F'),
         ('F','H'),('H','J'),('J','D'),('H','D'),('C','K'),('K','L'),
         ('L','M'),('M','P'),('P','Q'),('P','N'),('C','Q'),('L','Q'),
         ('C','P')]
    
    G = Graph()
    G.Set_directed(False)
    G.Set_weighted(False)

    for v,u in E:
        G.Add_edge(u,v)

    AuxiliaryGraph = Bicomponent(G, 'A')







 
      

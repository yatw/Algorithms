from PIL import Image
from Graph import Graph
from DepthFirstSearch import DFS


def BC(G,S):
    '''Construct an auxiliary graph that shows biconnected component'''

    Auxiliary = Graph()  # initially empty auxiliary graph
    
    explored_v, explored_e, back_edges = DFS(G,S) # run DFS once
    discovery_edge = [p for p in explored_e if p not in back_edges]
    examined_backedges = []

    Auxiliary.Initalize_vertices(discovery_edge)
    # add all discovery edges as vertices
    # all discovery edges are "unlinked"
    for v in explored_v:

        for be in back_edges:
            
            if v in be and be not in examined_backedges:
                print(v, be)
                
                examined_backedges.append(be)
                Auxiliary.Add_vertex(be)

                u = G.GetDestination(be,v)

                while (u != v):
                    possible_parents = G.FindParents(u)
                    u_index = explored_v.index(u)
                    
                    x = u_index -1
                    for i in range(u_index):
                        if explored_v[x] in possible_parents:
                            p = explored_v[x]
                            break
                        
                        x = x-1
                    #print('for u',u,'p is',p)
                    
                    #print('v',v)
                    #print('u',u)
                    #print(pp)
                    #print(explored_v)
                    #print('p',p)
                    f = (p,u)
                    print('-f',f)
                  
                    
                    if f not in Auxiliary.linked:

                        Auxiliary.linked.append(f)
                        Auxiliary.Add_edge((be,f))
                        
                        u = p
                        #print("new u",u)
                    else:
                        u = v
                    #print(Auxiliary.linked)
                
                
    return Auxiliary

if __name__ == "__main__":

    #image = Image.open('images\AuxiliaryGraph.PNG').show()
    V = ['A','B','C','D','E','F','H','J','K','L','M','P','N','Q']
    E = [('A','B'),('A','C'),('B','C'),('C','D'),('D','E'),('E','F'),
         ('F','H'),('H','J'),('J','D'),('H','D'),('C','K'),('K','L'),
         ('L','M'),('M','P'),('P','Q'),('P','N'),('C','Q'),('L','Q'),
         ('C','P')]
    G = Graph(V,E)

    r = BC(G, 'A')
    rv = r.vertices
    re = r.edges

    for v in rv:
        print(v)

    print("*"*20)

    for e in re:
        print(e)
  

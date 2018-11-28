

def QuickSelect(l,k):
    '''Returns a kth smallest item from the list'''

    n = len(l)
    if n == 1:
        return l[0]

    L = []
    E = []
    G = []

    m = l[len(l)//2]  # just pick the middle element
    
    for i in l:
        if i < m:
            L.append(i)
        elif i > m:
            G.append(i)
        else: #i == m
            E.append(i)

    if k <= len(L):
        return QuickSelect(L,k)

    elif k <= len(L) + len(E):
        return m

    else:
        return QuickSelect(G,k-len(L)-len(E))

    




l = [1,2,2,2,4,4,5]
print(QuickSelect(l,5))

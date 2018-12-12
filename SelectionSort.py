import math

# run time always O(n^2)


def SelectionSort(A):
    '''
        *Repeatedly (for i from 0 to n-1) find the minimum value
         output it, delete it
    '''

    
    result = []
    
    for i in range(len(A)):
        
        minimum = math.inf
        
        for e in A:
            if e < minimum:
                minimum = e
        result.append(minimum)
        A.remove(minimum)
        
    return result

if __name__ == "__main__":
    print(SelectionSort([23,19,42,17,85,38]))

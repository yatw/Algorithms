# Storage in place O(1)
# worst case running time, A[i] compare with at most i-1 elements O(n^2)
#

def InsertionSort(A):
    '''
        *Work from left to right across array
        *Insert each item in correct position with respect to (sorted)
         elements to its left
        *modify and return the given Array 
    '''

    for i in range(1, len(A)):

        c = A[i] # current element
        p = i-1  # index of previous element

        # shift the bigger element to the back
        while (p >= 0 and c < A[p]):
            
            A[p+1] = A[p]
            p -= 1

        # shift it all the way front
        A[p+1] = c

        
    return A

if __name__ == "__main__":
    print(InsertionSort([23,19,42,17,85,38]))

# Worst case O(n^2), if we pick a bad splitpoint every single split
# Average case O(nlogn)
# Improve Quicksort
# -- better choice of pivot element
# -- reduce procedure call overhead, manipulate stack instead of making recrusive call
# -- Reduce stack space


def QuickSort(A,first,last):
    '''
        Pick a pivot element, split groups, and sort each group

    '''
    if first < last:
        
        splitpoint = Split(A,first,last) # find split point
        QuickSort(A,first, splitpoint-1)   # sort first half
        QuickSort(A,splitpoint+1,last)     # sort second half
        
    return A

def Split(A,first,last):
    '''
        Find splitpoint, rearrange elements according to the
        split element, smaller element in front of splitpoint,
        bigger element after splitpoint
    '''
    splitpoint = first 
    split_element = A[first]

    # swap all smaller elements to behind split element
    # keep counting how many smaller element swaped
    # swap the split element with the number of smaller swapped
    # then end up with small element in the front, big element in the end
    for k in range(first+1,last):
        
        if A[k] < split_element:
   
            temp = A[k]  # swap with the element behind count
            A[k] = A[splitpoint+1]
            A[splitpoint+1] = temp
            splitpoint += 1
            
    temp = A[first]
    A[first] = A[splitpoint]
    A[splitpoint] = temp
    
    return splitpoint

if __name__ == "__main__":
    print(QuickSort([23,19,42,17,85,38], 0, 6))

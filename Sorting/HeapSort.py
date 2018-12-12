from BinaryHeap import BinaryHeap

'''
Storage is O(1),inplace

Heapify run in O(n) time
All calls to ExtractMax() require Remove, Remove require Shiftdown

total time is O(nlogn)

'''
def HeapSort(A):
    '''
        Continuely call ExtractMax, which always return the root of heap
    '''

    h = BinaryHeap(A.copy())
    h.Heapify()

    for i in reversed(range(len(A))):
        
        A[i] = h.ExtractMax()

    return A

if __name__ == "__main__":

    print(HeapSort([13,23,18,94,42,12,37,81,52,56]))




           

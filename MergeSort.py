# Divide and conquer approach
# recurrence equation is

# T(n) = 2T(n/2) + n - 1 , if n > 1
#      = 0 , if n = 1

# a = 2, b = 2, k = 1, use simplified Method
# a = b, case 2
# (n^k)logn = (n^1)logn = nlogn

# T(n) = θ(nlogn)


def MergeSort(A,first,last):
    '''
        Split array into two equal subarrays
        Sort both subarrays recrusively
        Merge two sorted subarrays
    '''
    
    if first < last:
        
        mid = (first+last)//2 # take the floor
        MergeSort(A,first,mid) # sort first half
        MergeSort(A,mid+1,last) # sort second half
        merge(A,first,mid,mid+1,last)
        
    return A

def merge(A,first1,last1,first2,last2):
    '''
        Merge the two subarray so they are in order
    '''

    index1 = first1
    index2 = first2

    temp = []

    # Merge into a temp array until one array is empty
    while (index1 <= last1) and (index2 <= last2):

        if (A[index1] <= A[index2]):
            temp.append(A[index1])
            index1 += 1
        else:
            temp.append(A[index2])
            index2 += 1

    # Copy the left over arrays
    while (index1 <= last1):
        temp.append(A[index1])
        index1 += 1

    while (index2 <= last2):
        temp.append(A[index2])
        index2 += 1

    # Copy the temp array back to the original Array
    i = first1
    for t in temp:
        A[i] = t
        i += 1

    return None

    
if __name__ == "__main__":
    print(MergeSort([23,19,42,17,85,38], 0, 5))



           

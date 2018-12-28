from PIL import Image

'''Example use even number of n for easier pairing'''
def MaxAndMin(A):
    '''Find both the max and min elements using
       3(n/2 - 1) + 1 time complexity

        Split into pair, compare the first pair, bigger element become running max
        smaller element becomes running min.
        For all following pairs, compare them and compare their result
        with running max and min
    '''

    running_max = None
    running_min = None
    
    first_pair = (0,1)
    if (A[0] > A[1]):
        running_max = A[0]
        running_min = A[1]
    else:
        running_max = A[1]
        running_min = A[0]


    next_pair = (first_pair[0] + 2, first_pair[1] + 2) # the index

    while (next_pair[1] <= len(A)-1):

        element1 = A[next_pair[0]]
        element2 = A[next_pair[1]]

        if ( element1 > element2):
            pair_max = element1
            pair_min = element2
        else:
            pair_max = element2
            pair_min = element1

        if (pair_max > running_max):
            running_max = pair_max
        if (pair_min < running_min):
            running_min = pair_min

      
        next_pair = (next_pair[0] + 2, next_pair[1] + 2)
   

    return running_max, running_min

if __name__ == '__main__':
    
    maximum, minimum = MaxAndMin([64,41,53,62,68,60,75,63])
    print("Maximum =",maximum,"Minimum =",minimum)

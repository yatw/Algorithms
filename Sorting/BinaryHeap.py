
class BinaryHeap:
    '''
        Elements are stored in an array
        Correspond to a binary tree in level order
        For any element v other than the root:
            parent(v) > v
            parent larger than child
    '''
    
    A = []
    
    def __init__(self, array = []):

        self.A = array

    def FindMax(self):

        if len(self.A) == 0:
            return None
        
        return self.A[0]

    def ExtractMax(self):
        '''Find maximum element and delete it'''

        if len(self.A) == 0:
            return None

        m = self.A[0]
        self.Delete(m)
        return m

    def LeftSon(self, E):
        '''Return left son of element E'''

        i = self.A.index(E)
        leftson_index = 2*i+1

        if (leftson_index > len(self.A)):
            return None
        
        return self.A[leftson_index]

    def RightSon(self, E):
        '''Return right son of element E'''
        
        i = self.A.index(E)
        rightson_index = 2*i+2

        if (rightson_index > len(self.A)):
            return None
        
        return self.A[rightson_index]

    def Parent(self, E):
        '''Return the parent of element E'''

        i = self.A.index(E)
        parent_index = (i-1)//2
        return self.A[parent_index]

    def ShiftUp(self, E):
        ''' Move the element at index i to its correct position up
            by repeatedly swapping the element with its parent
        '''

        i = self.A.index(E)

        if (i == 0):
            return None
        
        parent_index = (i-1)//2 # take floor
        if (parent_index >= 0) and (self.A[parent_index] < E):

            # if its parent is smaller, swap place with its parent
            self.A[i] = self.A[parent_index]
            self.A[parent_index] = E

            # continue to compare E with its grand-parent
            self.ShiftUp(E)

    def ShiftDown(self, E):
        ''' Move the element at index i to its correct position down
            by repeatedly swapping the element with its larger child
        '''

        n = len(self.A)
        i = self.A.index(E)
        left_child_index = i*2+1
        right_child_index = i*2+2

        # if a right child exist and it is bigger than left child, it is larger
        if (right_child_index < n) and (self.A[right_child_index] > self.A[left_child_index]):
            larger_child_index = right_child_index
            
        # otherwise use left child
        else:
            larger_child_index = left_child_index

        # if child exist and E is smaller:
        if (larger_child_index < n) and (E < self.A[larger_child_index]):

            # swap their places
            self.A[i] = self.A[larger_child_index]
            self.A[larger_child_index] = E

            self.ShiftDown(E)

    def Insert(self, E):
        '''Putting a new element and adjust element positions'''
        self.A.append(E)
        self.ShiftUp(E)

    def Delete(self, E):
        '''Swap place between deleting element and the last element
           move the last element to the correct position,
           remove the last node
        '''

        n = len(self.A)
        i = self.A.index(E)
        
        # put the last element into where E currently is
        # if we are removing the last element, this will do nothing
        last_element = self.A[n-1]
        self.A[i] = last_element
        self.A[n-1] = E

        # remove the element at the end of the list
        self.A.remove(E)

        if last_element in self.A:
            
            self.ShiftUp(last_element)
            self.ShiftDown(last_element)

    def Heapify(self):

        for i in reversed(range(len(self.A)//2)):
            self.ShiftDown(self.A[i])
        
        
    
if __name__ == "__main__":



    h = BinaryHeap([13,23,18,94,42,12,37,81,52,56])
    h.Heapify()
    print(h.A)



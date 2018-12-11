


def SelectionSort(l):

    
    result = []
    
    for i in range(len(l)):
        
        maximum = -1
        for e in l:
            if e > maximum:
                maximum = e
        result.append(maximum)
        l.remove(maximum)
        
    return result

if __name__ == "__main__":
    print(SelectionSort([4,9,4,2,3,2]))

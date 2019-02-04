from QuickSelect import QuickSelect
from SelectionSort import SelectionSort



def BruteForceSelect(S,k):
    ''' len(S) is guarteen to be less than 5'''

    s = SelectionSort(S)
    return s[k-1]


def DeterministicSelection(S,k):

    n = len(S)

    if (n <= 5):
        return BruteForceSelect(S,k)

    # Step 1 Divide S into groups of 5
    all_groups = []
    group = []
    for i in range(n):

        group.append(S[i])

        if (len(group) == 5):
            all_groups.append(group)
            group = []

    if len(group) != 0:
        all_groups.append(group)

    #print(all_groups)
    # Step 2 Compute median of each group
    group_medians = []
    for g in all_groups:
        
        group_medians.append(BruteForceSelect(g,1+(len(g)//2)))

    print(group_medians)
    # Step 3 Compute m* using recrusive call
    m = DeterministicSelection(group_medians,1+(len(group_medians)//2))
    print(m)
    # Step 4 and 5 is same as normal quickselect
    return QuickSelect(S,k,m)

if __name__ == "__main__":
    
    S = [29,90,93,14,11,
         38,22,81,91,17,
         62,83,97,64,66,
         26,55,89,51,24,
         32,78,66,47,61,
         76,82,70,85,73,
         15,99,86,13,88]

    x = DeterministicSelection(S,18)
    print(x)
 

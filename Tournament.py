from PIL import Image

'''Example use even number of n for easier pairing'''
def Tournament(A):
    '''Tournament algorithm find the second-largest element using
       n-1 + log(n) - 1 = n + log(n) -2 time complexity '''

    compared_with = {} # dictionary: {winner: [items compared with]}
    winners = A # initalize everyone is winner, slowly remove elements until 1
    n = len(winners)
    
    while len(winners) != 1: # haven't determine the winner yet

        losers = []
        index = 0
        for i in range(len(winners)//2):
            
            if (winners[index] > winners[index+1]):
                losers.append(winners[index+1])  # keep track of losers

                if winners[index] in compared_with:
                    compared_with[winners[index]].append(winners[index+1])
                else:
                    compared_with[winners[index]] = [winners[index+1]] # save the compare history
                
            else:
                losers.append(winners[index])

                if winners[index+1] in compared_with:
                    compared_with[winners[index+1]].append(winners[index])
                else:
                    compared_with[winners[index+1]] = [winners[index]]
                
            index+=2

        for l in losers:
            winners.remove(l)

    # now 1 winner is found, we look at compare history and find the largest
    
    second_max_candidates = compared_with[winners[0]]

    second_max = -1
    for sm in second_max_candidates:
        if sm > second_max:
            second_max = sm

    return winners[0],second_max

if __name__ == '__main__':
    
    image = Image.open(r"images\tournament.png").show()
    m,sm = Tournament([64,41,53,62,68,60,75,63])
    print(m,sm)

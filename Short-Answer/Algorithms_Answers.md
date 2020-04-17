#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
- there is one loop


b) O(n^2)
- there is a loop of loops


c) O(n)
- single recursion

## Exercise II

def find_f(n):
    # base case: egg breaks at first floor
    # drop egg at floor 1
    # have a variable that will return T/F called egg_broken
    if egg_broken:
        return 0

    ###### other cases ######
    ###### binary search ####
    # define range
    start = 0
    end = n
    middle = (start + end) // 2 

    # want to find two floors next two eachother where
    # the egg breaks and doesn't break
    # set fake numbers that wont get in the way
    highest_f_not_broken = -10
    lowest_f_broken = 2 ** 1000

    while (highest_f_n_broken - lowest_f_broken) != 1: 

        # drop egg at middle floor
        if egg breaks:
            egg_broken = True
        else:
            egg_broken = False

        # if egg breaks that means we're above f    
        if egg_broken:
            end = middle - 1
            
            # update the var that tracks lowest floor broken
            if middle < lowest_f_broken:
                lowest_f_broken = middle

            middle = (start + end) // 2

        # if egg doesn't break that means we're at or below f    
        else: 
            start = middle + 1
            
            # update the var that tracks highest floor broken
            if middle > highest_f_not_broken:
                highest_f_not_broken = middle

            middle = (start + end) // 2
        
        # keep dropping eggs until we reach a highest floor where the egg is not broken that is 1 floor away from where the egg is broken

    return highest_f_not_broken


Binary search
Time complexity is O(log(n))


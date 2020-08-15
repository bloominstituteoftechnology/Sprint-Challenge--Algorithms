#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n) - One loop. The runtime increases linearly with the size of the input data.

b)
    O(nlogn) - Two Loops. First loop is O(n), inner loop is O(log n) since the j is being doubled constantly, making it rise exponentially. 


c)
    O(n) - Recursion. 

## Exercise II

    The preferred algorithm which I would use is binary search. We would have to start at the middle floor of the n-story builiding, where we would throw the egg from. If the egg happens to break, then we would move down to the lower half of the building until the egg is able to fall without breaking, determining our f value. If the egg does not break when thrown from the middle, then we would continue towards the upper half of the building until it does break, which would then determine the f value. The runtime complexity would be O(log n). 

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 'a' representing a value , initialize a = 0. 
    while a is less then n^3
    reassign 'a' to n^2
    runtime O(3^n) ( triples the runtime each step)
    0(n)


b) initalize sum = 0
    for every i in sequence of n 
    set j to 1
    while j is less than sequence n 
    set j *= 2
    increment sum +=1 
    runtime O(n^2)
    0(n log n)



c) create a function passes var
    if var equals 0
    return 0
    runtime 0(n) 1 loop 

## Exercise II

* Binary search 0(log n)
- Sort through each (L, R) side of the tree until I get to the middle 
- Total # "dropped" eggs at midpoint 
- Then I once I get to the middle I would continue that binary search until I reach "below" the F floor to get the value of F

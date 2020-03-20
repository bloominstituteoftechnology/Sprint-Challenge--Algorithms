#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The number of operations is bounded by a multiple of n.


b) O(n^2) - The inner loop's n relies on the parent loop.


c) O(n) - Recursion functions act like loops and loops are linear.

## Exercise II

floor f or higher = broken egg
Below floor f = unbroken egg

def value_of_f(n):
    floor = 0
    broken_eggs = 0

    for loop for the floors starting from the bottom:
        while broken eggs greater than zero:
            if dropped egg doesn't break:
                floor += 1
            if eggs breaks:
                broken_eggs = 1
    
    return the value of the floor

Runtime complexity = O(n^2) 

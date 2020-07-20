#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): Linear Iterative Function, with duration tied to n value.

b) O(n^2): Quadratic Iterative Algorithm, run time grows proportionally to the length of n*n.

c) O(n): Linear Recursive Function, with duration tied to n value.

## Exercise II
    We want to minimize broken eggs, and we know that the eggs will remain unbroken below f. It can be assumed that in most cases minimizing broken eggs will inherently also minimize the number of drops, assuming your search is efficient.
    Therefore we want to start at f = 1, the floor above ground level, and continue to increment by 1 floor up until the egg breaks.
    Runtime: O(n) Broken Eggs: 1
    (If we tried searching by starting at the top floor, middle floor, and/or moving in larger increments then our runtime would be variable but likely more than 1 broken egg.)

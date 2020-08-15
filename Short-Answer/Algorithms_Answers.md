#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Raising a to the n^3, and increasing a by n^2 each loop will always be completed in (n) iterations, therefore the runtime complexity of the algorithm would be linear - O(n)


b) Begin with the for loop with a linear time complexity, consider that within the for loop exists a while loop which spans `j` to `n` for each iteration of the for loop incrementing `j` in exponential fashion therefore an increase in `n` represents a logarithmic function therefore the time complexity should be considered quasi-linear - O(n log n)


c) A recursive function which will always recurse `n` times and `n + 1` iterations, therefore the runtime complexity is linear - O(n)

## Exercise II

The question essentially ask for an implementation of the binary search algorithm which has a linear runtime complexity. O(n)

#### Implementation

- Find the middle floor of the building by dividing the total number of floors by 2
- If the egg breaks at that height, find the next middle floor, if it does not break go up to the floor half way between current floor and the roof.
- Repeat until egg breaks after having not broken



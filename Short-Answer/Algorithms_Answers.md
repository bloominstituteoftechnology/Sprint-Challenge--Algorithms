#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The number of operations is bounded by a multiple of n.


b) O(n log n) - The inner loop increases at a multiple of a constant.


c) O(n) - Recursion functions act like loops and loops are linear.

## Exercise II

floor f or higher = broken egg
Below floor f = unbroken egg

Binary Search would start on the middle floor. 
If on the new middle floor the egg doesn't break, the floor below it can be ignored.
If on the middle floor eggs are still breaking, the middle floor and all the floors above it can be ignored. 
This will continue until floor f is found.

Runtime complexity = O(log n) 

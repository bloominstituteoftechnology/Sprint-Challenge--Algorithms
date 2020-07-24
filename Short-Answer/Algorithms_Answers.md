#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n)
Time is dependent on the the size of n

b) 0(n^2) 
Nested loop, doing proportionally more work depending on what n is

c) 0(n)
Runs as many times as what bunnies equals

## Exercise II

Binary search, runtime complexity of O(log n):

Get the midpoint of the floors. 
Depending on if the egg breaks or not, split the floors in half and do the same.
If it breaks, pass in minimum and the middle. If it doesn't break, pass in maximum and middle.
Keep checking the middle of the passed in arguments, and once the two arguments are the same number, return it as f

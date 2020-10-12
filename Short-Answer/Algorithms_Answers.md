#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n)
There is only one loop so runtime is O(n) or linear run time.


b)O(n log n)
there is a while loop inside a for loop hence runtime is O(n log n)

c)O(n)
This is a recursive function 

## Exercise II

f represents lowest floor from where eggs break when tossed from it.
n represents number of stories in the building
f-1 represents floor from where eggs do not break when tossed.
Problem to solve:
find floor f from where eggs will break
if its 0 eggs will not break (initialization)
if dropped from nth floor it will break
Solution:
Best way would be to use binary search first a mid point can be set by using 0+n/2 next is to test if it breaks if not move right of midpoint, if yes then move left.
while loop and conditional if statements can be used to solve this problem.
Time complexity of this problem would be O(log n)

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n) linear, non-nested while loop.

b)
O(n^2)
nested loops are O(n^2)

c)O(n) (linear)
recursive function call

## Exercise II
We'll use a binary search tree
We need to check if eggs break at the midpoint, then, if they don't, check if they break at the midpoint between the midpoint and the end, and keep doing this until we determine where they do. If they do break at the midpoint, we'll determine the first floor where they break by checking the midpoint between the first index and the midpoint, finding the halfway point until we find the first floor where they break (and incrementing by 1 when we can no longer get an even midpoint). 
The runtime complexity is O(log(n))


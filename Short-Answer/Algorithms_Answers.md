#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity is O(n) because 'n' increases in size by one 

b) Runtime complexity is O(n) because here we have nested loops.  The first loop runs 'n' times and second loop is not re-iterating only using it as a comparision.


c) Runtime complexity is O(n) because here it's calling the recursive function which will call itself 'n' times. We are returning a constant value and not looping over anything even if you are recursing one.

## Exercise II

Since we are aware of the floors and are sorted, recommend using binary search, start on the middle floor and drop an egg. if the egg breaks, then move to middle of the floors below and repeat. If the egg doesn't break, move to the middle of the floors above and repeat. 
O(logN)

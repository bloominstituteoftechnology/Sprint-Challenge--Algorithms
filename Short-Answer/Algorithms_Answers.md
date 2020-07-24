#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime: O(n^c)
Justification: Inside the while loop n is multiplied (n^3). 


b)Runtime: O(n log n) 
Justification: The first part of the function is O(n), but inside the while loop the conditional value doubles until it is >= to n. 


c)Runtime: O(n)
Justification: The recursive function would scale linearly as the value of 'bunnies' increases.

## Exercise II

Proposal: I would use a binary search to solve this problem. Taking the length of the # of floors and then    // 2 to get the midpoint. Then 'drop' the egg in the middle if it breaks, eliminate the top floors, if it doen't break, eliminate the bottom floors. Then keeping dividing the floors in half in this manner until the highest safe floor is found.



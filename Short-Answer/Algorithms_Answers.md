#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

b) O(n^2)

c)O(c^n)

## Exercise II

input - n-stories
iterate over len(n-stories)
drop egg from the mid-point of n-stories
if it breaks
go drop another egg from midpoint between n-stories[0] and old midpoint - 1
else if it doesnt break
go drop another egg from midpoint between
old midpoint + 1 and n-stories[-1]
if the egg breaks at the last comparison then optimal floor is the lower one
if the egg doesnt break at the last comparison then it is the higher one

#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n^3) since (n _ n _ n)

b)O( n log n)

c) O(n) since function runs recursively for nth of times

## Exercise II

We can perform binary search in this case, where n is number of florrs in the building

pseudo code:

finding mid:
mid = floors / 2 - splitting top and bottom midway

lower_floors = floors[:mid +1 ]
top_floors = floors[mid + 1 ]

if egg breaks, do same test on the loser floor

else if egg doesnt break, do the test again on the top floor

return n

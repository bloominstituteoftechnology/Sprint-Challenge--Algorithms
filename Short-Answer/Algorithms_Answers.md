#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - single loop


b) O(n^2) - nested loop, rest are constants
even though j doubles, it is still dependent on n


c) O(n)

## Exercise II

you can divide and conquer since it will either be less or greater than a single floor

get middle floor of building
drop egg
if it breaks, top half inclusive gets removed
  find half again, repeat
if it does not break, bottom half inclusive gets removed
  find half again, repeat

this will be O(log n)
since it is dependent on n but it divides
you can prob solve this with iteration or with recursion


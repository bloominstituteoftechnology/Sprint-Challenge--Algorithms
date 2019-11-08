#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The reason that this is O(n) is because when you run through the loop, a grows at constant n^2 and the limit of the loop is at
n^3. This will mean that worst case is n^3/n^2, which works out to O(n).

b) O(n^2) - The reason is that within each for loop iteration, the while loop will run n // 2 times. So the total run time is n * n // 2
which makes it n^2.

c) O(n) - The reason is that the recursion is called n times plus 1. This still maintains the O(n) time.

## Exercise II
To solve this problem, a binary search can be applied.
Pseudocode:

check n//2 floor to see if egg breaks
if egg breaks:
  take the lower half and split that half to run check again
if the egg doesn't break:
  take the upper half and split that to check again
Keep checking until the prior f + 1 breaks and f does not

The runtime for this is O(log n). Because we are using binary search, we are splitting the search grid in half on each pass.

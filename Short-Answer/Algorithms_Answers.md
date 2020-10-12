#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The complexity of this code is O(n), or linear. It contains just a single while loop.


b) This code has a complexity of O(n^2). It is a for loop with a nested while loop, both of which have O(n) complexity. They are multiplied in this configuration, returning O(n^2).


c) The complexity of this code is also O(n), but for different reasons than in Example a. It uses recursion to try to reach the base case, therefore O(n).

## Exercise II

One good way to solve this is to use something very similar to binary search:

-Find midpoint of the n-story building.
-Drop an egg.
-If it cracks, find the new midpoint between the current midpoint and the ground and try again.
-Repeat until the egg does not crack. This is your solution.
-If it does not crack, find the new midpoint between the current midpoint and the top of the building.
-Repeat until the egg cracks. The highest you go before this happens is your solution.

Note: if the midpoint is halfway between floors, round down. This avoids splitting over and over into infinity getting smaller and smaller.

The complexity of an algorithm like this is O(log(n)), just like binary search.

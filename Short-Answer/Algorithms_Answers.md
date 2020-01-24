#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n) because the value of n determines how many operations are performed. For instance, when n is 5 there are 5 operations, and when n is 3 there are 3 operations.


b) This is O(n). When n is 5, sum is incremented to 15, which would be O(3n). And when n is 10, sum is incremented to 40, which is O(4n). Since we are not concerned about constants, the time complexity is O(n).


c) This is O(n). 

## Exercise II

I would use a binary search algorithm to find the highest floor where the eggs don't break. I would start by dividing n in half, and dropping an egg from the middle floor. If the egg breaks I know I don't need to test any of the higher floors and then divide the lower floors in half and try again. If the egg doesn't break from the middle floor, then I know that the egg won't break from the lower floors, so I eliminate them from the test and divide the higher floors in half and repeat the experiment from the new middle. Each iteration of the experiment I'm discarding half of the remaining floors until I reach the highest floor an egg can drop from without breaking.

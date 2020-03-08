#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n) - code will run once no matter what the size of n is and will only repeat once the while loop starts - the code is linear


b) This is O(n). When n is 5, sum is incremented to 15, which would be O(3n). And when n is 10, sum is incremented to 40, which is O(4n). Since we are not concerned about constants, the time complexity is O(n).


c) 0(n^2) - a nested while loop will make 0(n) multiply by itself

## Exercise II

I would use a binary search algorithm to find the highest floor where the eggs don't break. I would start by dividing n in half, and dropping an egg from the middle floor. If the egg breaks I know I don't need to test any of the higher floors and then divide the lower floors in half and try again. If the egg doesn't break from the middle floor, then I know that the egg won't break from the lower floors, so I eliminate them from the test and divide the higher floors in half and repeat the experiment from the new middle. Each iteration of the experiment I'm discarding half of the remaining floors until I reach the highest floor an egg can drop from without breaking.


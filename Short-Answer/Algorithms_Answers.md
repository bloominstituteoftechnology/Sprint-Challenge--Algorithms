#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - because the calculations are really based on a single value for n


b) O(n^2) - because there are two loops involving n and j


c) O(n) - because the recursion decreases each time through.  Even though the space complexity is not as good with recursion

## Exercise II

I would start at the middle floor and see if an egg breaks from there.  If not, then I can instantly exclude all the floor below from consideration and only check the top half of the floors.  I would then take my resulting top floors and divide them in half again and throw an egg from there and continue until I found the right floor.  This should give O(log n) runtime
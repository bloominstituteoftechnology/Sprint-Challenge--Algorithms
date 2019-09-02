#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - because the calculations are really based on a single value for n


b) O(n^2) - because there are two loops involving n and j


c) O(n) - because the recursion decreases each time through.  Even though the space complexity is not as good with recursion

## Exercise II

I would start at the first floor and throw an egg seeing if it broke.  Then I would go up, a floor at a time, throwing an egg to see if it breaks.  Once an egg breaks, then I would know the earliest floor that an egg breaks on.  The time complexity would be O(n) because I am iterating over the building stories loop only once to find my answer.
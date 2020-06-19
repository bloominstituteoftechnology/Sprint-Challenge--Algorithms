#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime for this problem is O(2^n) Exponential Time. The problem will take more time as the input size n gets larger.

b) The runtime for this problem is O(n^2) Quadratic Time because it is a loop within a loop.

c) The runtime for this problem is O(n). It is recursive, but is called based on the number of elements.

## Exercise II

I would use a binary search technique to find the floor where the egg breaks while also using the least amount of eggs possible. Using this technique, I would determine the mid floor of the n-story building and drop the egg from that height. If it didn't break, I would continue up the building, halving the distance to the top until the egg broke, then using the same technique down to find the minimum height that the egg breaks. This would be O(log n) runtime.
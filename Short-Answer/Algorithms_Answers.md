#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime is O(n). The size of a grows with the size of n


b) The runtime is O(n^2). Quadratic time because it is a nested loop within a loop.


c) The runtime for (c) is O(n). This one is recursive but is called based on the number of elements.

## Exercise II


runtime will be -- O(log n)

I would use the binary search technique to find the floor where the egg breaks while also using the least amount of eggs. 
By doing this I would be able to find out the mid floor of the n - story building and drop the egg from that height. If it does not break, I would continue up the building, 
halving the distance to the top until the egg broke, then use the same technique to find the maximum height that the egg breaks. 
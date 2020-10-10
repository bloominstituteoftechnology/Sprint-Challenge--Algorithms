#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

The function will run exactly n times. ex: if n = 5, the function will run 5 times, as long as a is less than 125. On the first loop a will be set to 25, the second 50, on the 5, 125 and stop.

b) O(n^2)

While not exact thanks to the doubling of j, the runtime does curve ever sharper upwards as the numbers get larger as is typical of nested loops that both run until n. It is twice as slow as O(n) by the time n = 3.

c) O(n)

For an input size of n = 10, n = 15, n = 20 the algorithm does 11, 16, and 21 iteration respectively. This follows a linear line.

## Exercise II

If the goal is simply to have the least amount of dropped eggs be broken, an iterative approach where each egg is dropped from the lowest floor on up until 1 egg breaks would be the best approach, with a run time complexity of O(n).

If the goal is to have the lowest total of eggs dropped while trying to keep broken ones minimal as well, then the divide and conquer method would likely be best. A binary search, where you drop the egg from the middle floor and then if it doesn't break, discard the bottom half and drop in the middle of the top half, halving each time to the top or bottom depending on whether the egg did or did not break.

This would have a run time complexity of O(logn) and would be far faster than the iterative option with larger buildings.

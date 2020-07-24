#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The runtime complexity of this function would be considered O(n) since the while loop runtime will increase in a manner that is directly proportional to the size of the input n. This directly proportional relationship, or one to one ratio of input size to the number of operations is definitively representative of linear runtime.

b) The runtime complexity of this function would be O(n log (n)). The outer loop would have a runtime of O(n) because it is entirely dependant on the input size of n, which is linear. The inner loop will have a runtime complexity of O(log n) due to the fact that the iterator (j) is incremented by doubling its value with each successive loop. This doubling would therefor cause the loop to run in half the range of n. This halving of the inner loop signifies a runtime complexity of O(log n). So, together, O(n) for the outer loop and O(log n) for the inner loop would together represent an O(n log(n)) runtime complexity.

c) The runtime of this recursive function will be O(n). The function will run n times with n representing the number of bunnies. The only computation being done is decrementing the number of bunnies by one with each recursive call. Therefor this is a linear runtime of a 1:1 ratio of input size to number of computations to be performed.

## Exercise II

The algorithm I would use in this case would seem to be in line with a binary search, whereby we are able to eliminate half of the floors (f) each time an egg is broken, thus moving closed and closer to the highest floor that the egg can safely be dropped from without breaking.

start = 0
end = len(f)
middle = (start + end) // 2

By starting at the floor in the middle, we can drop the egg and if it breaks we can eliminate all floors above the middle. If it does not break we can eliminate all the lower floors and repeat the process.

Assuming the egg broke when dropped from the middle floor, we eliminate all the floors above middle and move to the new middle in the lower floors and drop the egg again.

start = 0
end = middle - 1
middle = (start + end) // 2

We repeat until we narrow the search to the maximum floor height from which we can drop the egg and have it survive.

This binary search function will execute with a runtime complexity of O(log n) due to the fact that we are halving the number of possible values of f with each subsequent execution. This halving of the number of computations required relative to the input size of n is indicative of an O(log n) runtime complexity.

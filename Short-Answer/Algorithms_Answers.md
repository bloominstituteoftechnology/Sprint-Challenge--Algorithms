#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The runtime for this problem is O(n) because the bigger the input gets, the longer it is going to take. 

b)
This problem has a quadratic runtime - O(n^2) because there are two nested loops, and it needs to perform an operation for each value in the input data

c)
This runtime is O(n). Although it is a recursive and has to compute bunnyEars(bunnies-1), it is still dependant on the number of elements. 

## Exercise II
If I'm tasked to find the floor where the egg breaks, but minimizing the amount of eggs broken, I would use a binary search. I would start off at the middle floor, drop an egg, if it breaks I would go down. However, if it didn't break, I would proceed upwards. The amount of distance I would travel each time in each direction would be in half so (low + high) / 2. I would repeat this process until I found the correct height.
The runtime is Logarithmic Time - 0(log n) 


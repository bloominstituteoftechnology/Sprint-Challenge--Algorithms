#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)It looks like that the answer is O(n^3) but n's are eliminated by a = a + n *n
which results rapidly decreases the amount it take for a to be greater than or equal to n,
so the answer would be O(n) Linear


b)First there is For Loop n number of iterations, 
Second within the For Loop there is While Loop iterating j to n every time, and j is being multiplied by 2.

The answer is linearithmic O(n log(n))

c) Looks like function is calling itself. so function recursively called number of bunnies, until the base case reached (bunnies iqual to 0) so the 
answer is O(n) Linear

## Exercise II
In this case i will use bin search method

How does the bin search method works? It basically takes the array find the middle of the array and tries if the eggs breaks. Lets say if it is positive then the sublist will instatiated and go through recursively with the bounds adjusted downwards. If not then it will adjust upwards until the length of the list is 1.

time complexity?
may be O(logn)


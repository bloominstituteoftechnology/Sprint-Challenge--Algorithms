#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This code runs while a (which is equal to a + n^2) is less than n^3. This actually results in the code running n times. For example, if n is 3, a will be 9 on the first pass, 18 on the second, and 27 on the next, terminating the loop. 
This means that the code running directly corresponds to the input size, which is O(n). 


b) This code has 2 loops, one of which (the for loop) corresponds linearly with input size n, and the second, nested while loop will almost always run fewer times than input size n, logarithmically. This is O(n log(n)) time. 


c) This recursive function runs linearly. The number of times the function is called is in direct, linear correlation to the input size, which is O(n). 


## Exercise II
This situation is a good one in which to use a binary search algorithm. First, I would find the midpoint between the ground floor and the top floor. I would then drop an egg from this floor. If it breaks, I would know to pick a lower floor, so would again pick a midpoint between where I had just dropped the egg and the ground level. If it didn't break, I would pick a midpoint between where I had dropped the egg from and the top floor. I would repeat this process until I was able to determine floor f. This algorithm runs in O(log(n)) time. 



# Answers to Short Answer Questions

A: The first one appears to be linear, since the while loop will get bigger depending on what N is, the computations will not increase

B: This appears to be O(N^2) since it has multiple nested loops and the computations will exponentially grow depending on how large n is. This is not efficient

C: This is going to be 2^n since this appears to be the Fibonacci sequence, and the number of calls will increase as n increases since this is a recursive function

## Exercise 2

To solve this problem I would need a database of data to determine of what floor the egg was dropped and whether or not the egg actually broke. I would want to sort the data out first into two different lists of whether or not the egg broke and what floor it was dropped off of.

The first part of the algorithm would be something like. If the egg broke push it into either list A or B.

Secondly, I would look at sorting each value in the broken list from largest to smallest. An algorithm. like quicksort would likely do decent at this point for the list.

I would then have the algorithm find the smallest value in broken eggs, subtract one and this would effectively be your answer given the dataset provided. You couldn't guarantee that any eggs wouldn't get broken past this level, but it is fair to conclude that given the data, this will be the best answer.

The runtime of this would be O(n log2 n) which is the runtime for quicksort, and it wouldn't be the best of runtimes, however, given that we first create two lists that reduces the number of items that will need sorted, this will reduce the runtime and make it a bit more efficient. A more efficient sort could be used if the data was large enough, but for this situation, the sample size should be relatively small.

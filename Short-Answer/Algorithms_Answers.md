#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n)
The loop is set up to run through a length that is n * n * n, which would give us n^3. This would suggest cubic time, except, a is incremented by n*n on each run of the loop, not 1. Because of this the difference between the increment and the overall loop length is n. So our runtime is O(n)

b)

O(n log n)
The outer loop is looping through n, and the inner loop is looping through log n, as the pointer is being multiplied by 2 each time, instead of incrementing by 1.

c)

O(n)
This algorithm is recursive, however it is only calling itself once, and this creates a for loop that counts n down by 1 each iteration.

## Exercise II

I think binary search would be best here. Using linear search would just start at the ground floor and work up to the nth floor until it found f in linear time, using binary search we can reduce the search to log n time. 

The floors are essentially a sorted array, where bottom floors are non-egg-breaking floors and the top floors are egg-breaking floors. We are just trying to find the point where they swap. We would start by dropping an egg from the middle floor and the middle floor + 1. If the lower of the two doesn't break, but the higher one breaks, than f is the middle floor + 1. 

If both eggs break, we would go half way towards ground level and repeat the process with two adjacent floors there. If both eggs do not break in our initial drop, we would go half way towards the roof and drop from two adjacent floors there. 

We would keep subdividing in this manner, halving the number of floors we are looking at until we find the floor that is the tipping point for eggs breaking. The runtime of this solution would be O(log n)

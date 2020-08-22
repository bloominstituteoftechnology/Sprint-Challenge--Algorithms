#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

## O(n)
a)  the loop is going to run n^3. Since a is incremented by n*n on each run of the loop, meaning the difference between this increment and the over loop length is n. 

## O(n log n)
b) Outer loop is looping through n, while the inner loop is looping through log n. This results of in the pointer is being multiplied by 2 each time. 

##O(n)
c) This algo is recursive. But it is only calling upon itself once. This results in basically a for loop that counts n down by 1 each time. 

## Exercise II

I believe binary search would work best for this problem opposed to a linear  search that would start atground floor and work up to the nth floor. Binary search will allow us to reduce the search to log n time. We start by dropping an egg from the middle floor and the middle floor + 1. if the lower of the two does not break the egg, but the higher one does, than f is middle floor + 1. 

However, if the eggs both break, we would go half way towards ground level and repeat the process. If both eggs do not break in the iniital drop, we would go half way towards the roof and drop from two adjancent floors. 

We would keep this process going, halving the nuber of floors we are looking at until we found the floor. 

Runtime = O(log n)




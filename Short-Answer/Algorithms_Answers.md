#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This algorithm runs in O(n) time; as the size of n increases,\
 the number of times the loop executes increases linearly.


b) This algorithm runs in O(n**2) time; the while loop nested inside the for loop\
will cause the time to increase roughly exponentially.


c) This algorithm runs in O(n) time; it is running a fixed number of times,\
 where if bunnies (n) = 1 it would execute in O(1) time. the recursive call will execute n-1 total times,\
 meaning the time to completion grows linearly with the increase of n as 1 + n-1.

## Exercise II

Binary search:\

Drop an egg off of floor n // 2 (n<sub>1</sub>);

if it breaks, f is below n<sub>1</sub>. If it doesn't break, f is above n<sub>1</sub>.\
continue dropping eggs from the midpoint of n<sub>k</sub> and the current floor or ceiling (n<sub>prev</sub>)\
until f is reached; this will lead to ~ k/2 eggs broken, with f found in k steps.\
runtime complexity is O(log n)



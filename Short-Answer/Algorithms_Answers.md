Add your answers to the Algorithms exercises here.
## Exercise I
a) O(n)

if n == 1:
The while loop would run 1 time.
if n == 2:
The while loop would run 2 times.
if n == 3:
The while loop would run 3 times.
And so and so forth.

b) O(n^3)
There are three for-loop that depend on n. The last for-loop runs a constant of 9 times.

c) O(n) This is basically a for-loop.

## Exercise II
I would use a divide and conquer approach, something base off of the binary search method. I would divide the floors in half, thrown an egg, check to see if broken. If the egg did break I would search the lower half of the floors, else I would search the higher have of the floors. I would repeat this process until I found _f_. The runtime complexity would be equivalent to the binary search method O(log(n))  
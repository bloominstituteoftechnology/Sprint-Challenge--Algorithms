Add your answers to the Algorithms exercises here.

I.
a) O(n\*\*2)
b) O(n!)
c) O(log n)

II.

I'd use something similar to a binary search method to find floor _f_. The first step would be to find the middle floor(mid1) of the building and drop the egg. If the egg didn't break, I'd move to the middle point(mid2) between my current floor and the top floor and drop it again. If the egg didn't break, I would repeat the process of using my current floor(mid2) as the base floor and going to the middle of that floor and the top floor. If the egg _did_ break after being dropped from that floor(mid2), I'd move to the middle floor between my current floor(mid2) and the building's middle floor(mid1).

If the egg broke from the middle floor, I'd carry out the process above but use the middle and bottom as the points defining the range instead of the middle and top floor.

The runtime of this approach is O(log n).

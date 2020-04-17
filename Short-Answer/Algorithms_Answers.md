#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3)
(A geometric math equation called n^3 times.)

b) O(n^2)
(A double nested loop)

c) O(n)
(A recursive function that counts linearly backwards from n to zero.)

## Exercise II

Let's attack the building like a binary search tree...

1. Go to the middle floor.
2. Drop an egg.
   a. If it breaks, go _down_ half the number of floors you did last time.
   b. If it doesn't, go _up_ half the number of floors you did last time.
3. Repeat from #2 until you are no longer changing floors.

You will finish your quest in **log(n) time**. (Where n is the height of the building in floors).

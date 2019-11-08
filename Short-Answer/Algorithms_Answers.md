#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
O(n) because the iterations increase linearly as n increases. For n = 1, 1^3 = 1, then terminates when a = 1^2. For n =2, 2^3 = 8 with iteration 1 (0 + 2^2 = 4) then iteration 2 (4 + 2^2 = 8).

| n | steps |
-------------
| 0 | 0 |
| 1 | 1 |
| 2 | 3 |
| 3 | 3 |


b)
O(n^2) - Nested loops will result in n^2 runtime


c)
O(n) This runs linearly because it reduces n-1 times until the bunnies are 0 

## Exercise II

Try to minimize DroppedEggs

1. Start with variable that detects BrokenEgg and which floor, 
2. Start at the first floor
3. While the BrokenEgg is yes, drop again
4. If BrokenEgg is no, store the floor number



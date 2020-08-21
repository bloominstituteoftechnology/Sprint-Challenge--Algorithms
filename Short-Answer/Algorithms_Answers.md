#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0
    while (a < n * n * n):  --- N * (any non constant in while loop)
      a = a + n * n

O(n*n*n) = O(n^3)

Polynomial time complexity


b) sum = 0
    for i in range(n):  ---- N * (any non constant in for loop)
      j = 1
      while j < n:  --- N * (any non constant in while loop)
        j *= 2
        sum += 1
 
 O(n^2)

 Quadratic time


c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

O(1)

Constant time - as the data size does not change the run time of the method (only the number of recursions, which is not a Big O factor)

## Exercise II

1 - Create properties for broken_eggs and dropped_eggs
2 - Loop through the number of floors
3 - Drop an egg on the current floor
4 - Check if the egg was broken
5 - If broken, move back one floor and drop the rest of the eggs (safely)
    Check case where egg breaks on floor 1
6 - If not broken, move to next floor and drop and egg 

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
## because the loop is dependant on the value of n

b) O(n^2)
## the nested for loop relies on the size of the n inside the loop

c) O(n)
## it's a recursive function until it hits zero that is being called and it relies on the value of bunnies

## Exercise II

I would use a Binary Search here

## Reason being you need to eliminate half of the floors, so you start in the middle floof then drop an egg. if the egg_broken = true then you proceed downward to the next floor and repeat the process. If the egg_broken = false after you drop an egg you move upward  and repear the egg drop. So it would be  O(logn)
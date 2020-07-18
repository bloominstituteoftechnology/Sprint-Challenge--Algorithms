#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Linear O(n) - The input increses at n^3 times, but a reaches n at n^2 times and stops the loop, runtime is O(n).


b)
Linearithmic O(n log n) - Outer loop is n, inner loop is log n because j is multiplied *2 each time so it reaches n in log n time and stops the loop.


c)
Linear O(n) - Steps required to complete execution increase linearly with the number of inputs (bunnies).


## Exercise II

Broken eggs can be minimized with a linear search strategy, starting from next to the ground floor and dropping eggs until the first floor when the egg breaks. This is floor f. This is O(n) runtime complexity.

The dropped eggs can be minimized by use of a binary search strategy, starting from the middle floor, depending on weather the eggs either break or not, going down or up by half of the remaining floors. So we keep doing this, always dividing by 2 the number of remaining floors, until reaching a point where there are two consecutive floors checked from which there are different outcomes: egg breaks from the higher of the two, doesn't break from the lower. These are floor f and floor (f - 1), the first egg-safe floor. 

Runtime complexity is O(log n).



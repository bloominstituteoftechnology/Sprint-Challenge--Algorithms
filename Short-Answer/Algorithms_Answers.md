#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)Linear O(n) - The input increses at n^3 times, but a reaches n at n^2 times and stops the loop, so overall runtime is O(n).


b)Linearithmic O(n log n) - Outer loop is n, inner loop is log n because j is multiplied *2 each time so it reaches n in log n time and stops the loop.


c)Linear O(n) - Steps required to complete the execution increase linearly with the number of inputs.

## Exercise II

Broken eggs are minimized with a linear search strategy, starting from next to the ground floor and dropping eggs until the first floor that the egg breaks. This is floor f. This had a O(n) runtime complexity.

Dropped eggs are minimized with a binary search strategy, starting from the middle floor, and depending on weather the eggs break or not, going down or up by half of the remaining floors of the building. We keep doing this, always dividing by 2 the remaining floors, until we reach a point where we have two consecutive floors checked from which we have different outcomes: egg breaks from the higher of the two, doesn't break from the lower. These are floor f and floor (f - 1), the first egg-safe floor. Runtime complexity is O(log n).

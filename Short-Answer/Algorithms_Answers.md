#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n<sup>3</sup> + n<sup>2</sup>)


b)  O(c<sup>n</sup>)


c)  O(c)

## Exercise II

First, I would create a list to represent the building up to floor _n_.  Throw an egg from the middle floor.  If it breaks, discard the top half of the list, and throw the egg again from the middle of the remaining floor.  If it does not break, discard the bottom half of the list, and throw the egg again from the middle of the remaining upper floors.  Keep it up until floor _f_ is the only floor left.

O(log n) runtime complexity

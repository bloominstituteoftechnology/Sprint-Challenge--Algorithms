#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)My analysis of this snippet's runtime is Linear, or O(n). We start at O(n^3),
but reduce by O(n^2) that is incrementing inside the loop. Thus making O(n). 

b)My analysis of this snippet's runtime is Logarithmic, or O(log n). As the size
of the input increases, the runtime also grows at a small rate.

c)My analysis of this snippet is Linear, or O(n). We only decrease bunnies at a
rate of 1.

## Exercise II
In order for this to work, we want to throw the eggs off of floors below floor 'f'.

To make this successfull, I would start with a Binary Search. This way, we start at
the middle floor and drop an egg. If the egg breaks, all floors above that can be
ignored, returning a new set of floors. Then we try again at the middle point of the
new floors, and if the egg doesn't break, the floors below that can be ignored, once
again shortening that list and repeating the process until we find where the egg
doesn't break on one floor, but it will on the floor directly above it. Due to the
continual halving of the floors, and with us using the Binary Search Tree,
the algorithm will be O(log(n)). 

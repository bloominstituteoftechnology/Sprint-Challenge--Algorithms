Add your answers to the Algorithms exercises here.

Algorithm answers:

Exercise I:

a) Runtime complexity: O(n)
Runtime is O(n) because the while loop is executing only one time for a given data set. The n number will be a large number as it is being multiplied, but it is still only executing one time for the data set.

b) Runtime complexity: O(n^3)
There are three nested loops that are being run that depend on the size of n. The fourth loop only runs a fixed number of times (<10) so has a constant run time. Each nested loop has a run time of O(n) so we multiply each to get the run time of the code.

c) Runtime complexity: O(n)
The bunnyEars function will get executed recursively until bunnies input reaches 0.

Exercise II:
Strategy: Treat the floors in the building as a sorted set of numbers and use divide and conquer to identify f by dividing by two the number of floors available.
Step 1: Go to the middle floor and throw an egg, check to see if the egg is broken.
If it is broken, all of the floors above can be eliminated.
If it is not broken, all of the floors below can be eliminated
Step 2: Go to the middle floor of the remaining floors and repeat step 1

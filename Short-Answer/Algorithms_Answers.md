#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This loop has a runing time of O(n). The while loop is ran based of n³ so it seems it's O(n³), but the "a" variable increment of n², making the loop running n times. To be even more clear f(x) = n*n*n/ n*n => f(x) = n => O(n)


b) The for loops runs n times and the nested while loop runs log²(n) making the big O notation for this snippet of code being O(n log(n))


c) This recursive function is called n times (where n is the number of bunnies) so it's big O notation is O(n)

## Exercise II

Probably the best solution here is using binary search. We can check the middle floor and if the eggs break we can repeat the process for the left part of the list (lowers floors), otherwise we can do the same for the upper floors. The big O notation for it is O(log(n)).

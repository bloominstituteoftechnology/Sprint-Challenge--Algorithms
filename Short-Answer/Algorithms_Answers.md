#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)The runtime is O(n^C)


b)The runtime is O(nlogn)


c)The runtime is O(n)

## Exercise II
Assuming no prior knowledge regarding eggs, gravity and so on, the optimal strategy for finding f with the condition that the value (dropped eggs + broken eggs) is minimized is a binary search.
First dropping an egg at the n/2 th floor, then recording the result. If the egg broke, we eliminate all higher floors as points of interest because of the properties of f. If the egg did not break, we eliminate all lower floors as points of interest.
Each time we drop an egg we do so from the middle of the range in which we have interest. This means that on average we eliminate possible answers as rapidly as we can.
The complexity would be O(logn) because we do not need to drop from every floor, and the larger the building is the more floors we need to consider.


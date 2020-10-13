#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I think that this while loop performs at O(logn) because a balloons over iterations, even if n can grow quickly as it is set to the 3rd power. 


b) I think this one is O(n log n) because it has an outer for loop and an inner while loop that multiplies by itself until it reaches a threshold. Each time the inner loop runs, it gets closer to the threshold in less than linear time.


c) I think this recursion is O(n) because larger numbers will take more recursions, but the recursive call is simple -- it only requires addition.

## Exercise II
While I am dropping eggs, if I drop an egg above floor f, it will break and I will count it. Otherise, it will not break and I will not count it as broken.

When I am done, I will return the ratio of cracked eggs over total eggs dropped.

Runtime: O(n)
#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). The loop should execute n times.


b) O(n log(n)). The outer loop runs n times. The inner loop runs log(i + 1)
times, where i is at most n - 1.


c) O(n). The function, called once by the user, will call itself n more times,
assuming n is a positive integer.

## Exercise II

1. Start at the ground floor, drop an egg. Move up one floor until the first
(lowest) floor from which a dropped egg breaks is found. In theory, this is
linear search, worst (and average) case O(n), best case O(1). In real life, we
can pretty typically expect best case performance here, since eggs do not
become more durable when dropped from higher buildings.

2. If this is not real life, use binary search on a sorted array, which has
complexity O(log n). If your building has unsorted floors, you have bigger
problems: Try a floor around the middle. If a dropped egg breaks, this floor is
the highest one you need to consider. Repeat the procedure for the sub-building
so defined. If it doesn't break, then the floor above is the lowest one in need
of consideration. Again, repeat the procedure for the sub-building so defined.
Eventually there will only be a floor or two remaining to check, at which point
the answer will be a trivial matter.
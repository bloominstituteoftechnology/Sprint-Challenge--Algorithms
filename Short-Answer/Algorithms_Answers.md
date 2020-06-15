#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^2) => a = a + n * n. The n * n is the highest n value.


b) O(n) => I want to say this is O(n) because the while loop has to iterated over every item until it hit j < n


c) O(1) => I want to say this is O(1) because the function is simply adding 2 to the what is left of (bunnies - 1)

## Exercise II
dropped_egg(n, f):
    if f > n // 2:
        return 'Broken Egg'
    else:
        return 'No Broken Egg'

Runtime: O(n)

This is assuming that above the midpoint of the building, the egg will break.
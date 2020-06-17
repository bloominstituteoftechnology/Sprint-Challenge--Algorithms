#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Here `n` is constant because we are just dealing with one loop.


b) O(n^2) - Here `n` has to go through a nested loop.


c) O(n) - Here "bunnies" or `n` is constant as well.

## Exercise II

n-story building

greater than or equal to F = Broken
less than F = Safe

Step 1: Go to middle floor
Step 2: Drop egg
    a: if egg breaks, go down one floor, repeat 2
        if egg does not break subtract dropped eggs(plus one) from middle floor to find floor F
    b: if egg doesn't break go up one floor, repeat 2
        if egg does break add number of dropped eggs to middle floor to find floor F

This solution appears to be O(n) because we are just dealing with one loop.
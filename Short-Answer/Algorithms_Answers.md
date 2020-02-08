#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

O(n)

The worst-case runtime of this block of code depends on the value of n, making
it linear.

b)

O(n^2)

Because there are two for loops, one nested inside the other and both up to `n`
times, this makes this block of code quadratic.

c)

O(n)

Technically this is O(n - 1) which is still linear. This block of code still
depends on the number of bunnies.

## Exercise II

Using a binary search approach:

1. determine the middle floor out of the total number of floors
2. drop the egg:

   a. if egg breaks, set highest floor equal to the middle floor

   b. if egg does not break, set lowest floor equal to middle floor

3. repeat steps 1 - 2
4. once you find point where egg breaks next does not you have found f floor

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n) because we're dividing n^3 by n^2 which is (n^ (3 - 2)) = n


b) 0(n), increasing j by 2 each time until it reaches n


c) 0(n), subtracting one at a time while adding two each time. Loop will iterate until n == 0

## Exercise II
Use a binary search to find the floor. Starting at the middle floor, if the egg breaks at that floor move to the bottom 1/2 of floors below that middle floor and go to the
middle floor. If the egg doesn't break at that point, then move to the top 1/2 of floors left between the first middle and second middle. Keep performing this operation until
you find the floor at which the egg doesn't break.
O(log(n))
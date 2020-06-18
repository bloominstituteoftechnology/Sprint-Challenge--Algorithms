#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): The while loop will run until a < n^3 and a is increasing by exponentially by n^2, this will run in o(n)


b) O(n^2) The outer loop will run n times and then inner loop will run n/2 times so n * n/2 is 1/2 n^2, which is o(n^2)


c) O(n) this recusion has a single call to the function each time through with n decreasing by 1 each time

## Exercise II
Start at f = 0. Drop an egg to see if it breaks. If not, drop and egg from position n to see if it breaks. If not, move to f = n - f / 2 (the middle). If an egg breaks go to the spot between n and f, if not,go to the spot between f and 0. Repeat until the correct f is found. This uses a binary search so n should be log(n)


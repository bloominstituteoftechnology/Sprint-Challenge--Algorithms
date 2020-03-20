#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N), because it's like a for loop that goes till n^3, but each step is n^2, so the loop will always take n increments to complete. For example, for n=2 the loop ends around 8, but increments by 4 every time, so 8/4 is 2, or n. It took n times to complete.


b) O(log(N)), because we have two loops multiplied together. The first loop is n, and the second loop is log(n), so n * log(n). The reason the nested while loop is log(n) is because its runtime complexity is halving every time, since j*=2.


c) O(N), because this acts like a fancy for-loop. It starts at n and increments down by one until n is zero. Every time it calls itself again, it decreased the number of loops left by one. The loop will always occur n times.

## Exercise II



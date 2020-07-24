#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear Time. O(n) because the output's value depend of the input size.

b) O(n^2) because we use two loops. So O(n) * O(n) = O(n^2). Quadratic Time 

c) Linear Time. O(n) because the output's value depend of the input size.
## Exercise II

1.Find the mid floor. 
2.If the egg breaks,check the lower half of the floors.(ignore the upper half)
3.If the egg doesn't break,check with the upper half. (ignore the lower half)
4.Then continue to recurse until we are left with two floors,low floor should not break, upper floor should break.

Time complexity: O(logN)
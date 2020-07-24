#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear Time. O(n) because the output's value depend of the input size.

b) O(N log N)

c) Linear Time. O(n) because the output's value depend of the input size.
## Exercise II

1.Find the mid floor. 
2.If the egg breaks,check the lower floors of the building.(ignore the upper half)
3.If the egg doesn't break,check the upper half floors of the building. (ignore the lower half)
4.Then continue to recurse until we are left with two floors,low floor should not break, upper floor should break.

Time complexity: O(logN)
#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    In each iteration 'a' value will increase by n*n. After n iterations 'a' value will be more than the "a < n*n*n" condition.
b) O(n * log(n))
    The outer loop will run n times and inner loop will run log(n) because 'j' value doubles every iterations of the inner loop and will become larger than n after log(n) iterations.
c) O(n) 
    This recursive function calls itself n times and only adds 2 to the return value which is constant time operation.

## Exercise II


    I would approach binary search method in this case.

    1. Find the middle floor mid = f/2
    2. Start dropping the egg from the middle floor = while loop
    3. Check if it is broken or not
    4. If it is broken then start decreasing the floor number by one until it stops breaking.
    5. If it is not broken then start increasing the floor number by one until it start breaking
   
    Since this is an binary search method by doing divide and conquer it will take O(log(n)) RTC.
    
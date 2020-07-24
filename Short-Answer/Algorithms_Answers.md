#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The time complexity will depend on the value of n.


b) O(n^2) - We have a loop within a loop, so the time complexity will be n* * *n = n^2


c)  O(n) - Again, will depend on the value of n.

## Exercise II

For this question, we could use a recursive binary search function
to find the value of f such that the number of dropped + broken eggs is minimized.
Since we’re only given n, we can use n to create a list of numbers from 

def recursive_function(n):
    list_of_floors = [0, 1, ..., n]
    choose middle point, and drop an egg
    if the egg breaks, the function will recurse using the lower half of the list
    if the egg doesn’t break, the function will recurse using the upper half of the list
    base case will be when the list is of length 1
    in which case, it will drop an egg and return either the single value in the list, or that value - 1.

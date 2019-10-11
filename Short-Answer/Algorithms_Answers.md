#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n) Linear Time :
The steps required to complete the execution of this function increase linearly with the number of inputs.



b)
O(n^2) Quadratic Time:
In this function we have an outer loop that iterates through all the numbers in range(n) and a nested
inner loop which again iterates through all numbers less than n. The total number of steps performed is 
n * n

c)
O(n) Linear Time :
bunnyEars function is being called recursively n times before reaching base case so its
number of operations increase linearly with the number of inputs.

## Exercise II

f = floor F "Eggs at this floor or higher will begin to break"

The given problem states that we are looking for a value "f" inside a list of floors in a building.
Given that floors in a building are inherently sorted we can use this to our advantage.
Since the floors are in order we could utilize Binary Search algorithm to find the value of "f".

1) REPEAT until you are left with two floors.
    2) We would start by throwing an egg off of the middle floor.
    3) IF egg breaks -> pick the middle floor of the levels LOWER than you. 
            Eliminate all HIGHER floors as a possibility.
    
    4) IF egg SURVIVES -> pick the middle floor of the levels HIGHER than you.
            Eliminate all LOWER floors as a possibility.

5) IF there are only 2 floors left AND the egg BREAKS from the floor you throw it off of then
    throw it off of the floor beneath you 
        IF it BREAKS j = the floor you are on
        ElSE it SURVIVES j = the floor you are on + 1

6) ELSE there are only 2 floors left AND the egg SURVIVES from the floor you throw it off of then
    j = the floor you are on + 1
    
Runtime Complexity = O(log n) Logarithmic time. We are dividing the possibilities by half every time the code loops therefore increasing time performance.
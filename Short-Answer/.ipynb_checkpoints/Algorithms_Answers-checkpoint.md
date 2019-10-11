#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) This code relies on a single loop executing n times. Therefore it is of linear complexity. 


b) O(n^2) This code relies on a nested for loop. For each run through of the alogithim, it executes O(n*n) times.

c) O(n) The function is going to be calculating `2 + bunnyEars(bunnies-1)` which is O(n) as the function is being called recursively n times before reaching base case. 

## Exercise II

This appears to be a search problem. In this case, we are trying to avoid a linear search where we break a lot of eggs. Therefore, I suggest a binary search, where we repeatedly divide the search interval in half. If the first interval results in `broken == True` the search the lower interval. If that interval results in `broken == False`, search the upper interval next. Continue dividing the array in half until the correct floor is found. 
 
This would run at O(log(n)) complexity. 

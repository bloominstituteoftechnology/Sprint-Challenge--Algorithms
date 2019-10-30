#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1*n) because the while loop will iterate exactly n times. 


b) O(n logn) 


c) O(n)

## Exercise II

Use Binary Search. Complexity is O(log n) because on each pass you're ruling out half the floors.
middle_floor = (highest_floor + lowest_floor) // 2
Drop an egg on the middle floor. If egg breaks, go to the midpoint floor between bottom floor and current floor. If egg does not break on middle floor, go to midpoint floor between top floor and current floor. Continue this process until the correct floor is found.

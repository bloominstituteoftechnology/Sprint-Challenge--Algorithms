#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(log n^3)

b) O(n^2)

c) O(n-1)

## Exercise II


Set up: Our low point would be 0 for the ground. Our high point would be "n" for the top of the building. Our midpoint would be "f" for the floor that the eggs can safely be dropped.

Base case: for each floor if the floor number is equal to or less than "f" and we have eggs to drop we will drop an egg.

If the floor number is greater than "f", then we do not drop and egg.

When there are no more eggs, we exit the function.

This algorithm should have a runtime complexity of O(log n).
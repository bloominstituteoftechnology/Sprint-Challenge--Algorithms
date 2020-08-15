#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
# O(n) - because there is just one loop, one pass.

b)
# O(n^2) - there is a nested loop. 

c)
# O(n) - this is recursive but linear, compared to the inputs.

## Exercise II

essentially we would need to iterate through the floors, having a high_floor, low_floor, and a current_floor. 

our first solution would involve a runtime complexity of O(log n) as we could theoretically make a shorter time to the solution by introducing a midpoint floor between the highest and lowest floors. We would set this as our current_floor that we would start tossing eggs down from.

we could say while the highest-lowest is greater than 1, if the egg doesnt break for the current story, set that as the lowest floor. We can then ask if the egg does break we can then set the current floor to the highest floor and return the current_floor as the floor that broke the egg. 


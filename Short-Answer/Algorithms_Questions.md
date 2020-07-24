# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
# O(n) - because there is just one loop, one pass.


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
# O(n^2) - there is a nested loop. 
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
# O(n) - this is recursive but linear, compared to the inputs.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

essentially we would need to iterate through the floors, having a high_floor, low_floor, and a current_floor. 

our first solution would involve a runtime complexity of O(log n) as we could theoretically make a shorter time to the solution by introducing a midpoint floor between the highest and lowest floors. We would set this as our current_floor that we would start tossing eggs down from.

we could say while the highest-lowest is greater than 1, if the egg doesnt break for the current story, set that as the lowest floor. We can then ask if the egg does break we can then set the current floor to the highest floor and return the current_floor as the floor that broke the egg. 
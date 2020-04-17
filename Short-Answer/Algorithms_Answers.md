#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) => There is only one loop.

a = 0
    while (a < n * n * n):
      a = a + n * n

b) O(n^2) => There is a nested loop

sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

c) O(n) => Recursive, but still linear compared to inputs

def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

## Exercise II

Set lowest_floor to 0
Set highest_floor to numbers of floors in the building
Set current_story to mid-point between highest and lowest floors (highest / lowest)
While highest-lowest > 1
If egg doesn't break from current story set current_story to lowest_floor
Elif egg does break set current_floor to highest_floor
return current_floor = breaking_floor

RC would be o(log n) from diving in half each time

1 2 3 4 5 6 7 8 9 10
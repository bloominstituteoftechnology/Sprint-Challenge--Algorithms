#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n^3), the number of loops is dependent on `n * n * n`

b)O(n^2), nested for loops based on `n` in both loops

c)O(n), Called recusively based on `bunnies - 1`, base case `bunnies == 0`

## Exercise II

1. Go to the middle floor
2. Drop an egg:
   a. If it breaks, go half way up the top remaining floors
   b. If it doesn't break, go half way down the bottom remaining floors
   Repeat step 2

```python
f = floors

def drop_at_midpoint(f):

    mid = current_floor = midpoint_of_floors
    t = top_half_of_current_floors
    b = bottom_half_of_current_floors

    if no_of_floors = 1:
        return current_floor

    if egg_breaks:
        drop_at_midpoint(b)
    else:
        drop_at_midpoint(t)
```

Time Complexity: O(log n), the number of possible floors is cut in half on each call of the recusive function
making it n^1/2, or log n

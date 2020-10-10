#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0 # O(1)
    while (a < n * n * n): # O(n^3)
      a = a + n * n # O(n^2)

# This block of code is O(n^3) since the while loop has 3 n's which basically equals to n^3
```

```python
b)  sum = 0 # O(1) 
    for i in range(n): # O(n)
      j = 1 # O(1)
      while j < n: # O(n) -> O(n^2)
        j *= 2 # O(1)
        sum += 1 # O(1)

# This block of code is O(n^2) since the while loop is nested inside the for loop. Both are linear independently 
# which, added together, makes them n^2.
```

```python
c)  def bunnyEars(bunnies): 
      if bunnies == 0:
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) # O(n)
# This block of code is O(n) because the bigger the input, the more recursive call stacks are required
# for this function. Or another of way of speaking it, the function increases linearly with the the size of the input.
```

## Exercise II

Simple, we use a binary search algorithm. Specially, we need a pivot, which we would make the middle of the building.
Then we would see whether we break an egg or not. If so, then we would go to a lower pivot of the building.
If not, then we would go higher to upper half of the building. We would continue doing this until we hit
a base case where we find the two floors where one breaks our egg and one doesn't. Then we just return the floor above.
This solution's runtime would be logarithmic time or O(log n).

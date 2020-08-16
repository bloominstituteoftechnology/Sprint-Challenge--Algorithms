# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

### Proposed Solution

I assume the goal is to find the highest floor in the n-story building from which an egg drop results in an unbroken egg. 
In that case the strategy could be:

1. Go to the equivalent of half way up the building: floor n/2
2. Drop an egg
3. Does the egg break?
4a. If the egg breaks, then go to the "halfway" point in the lower half of the remaining building: floor (n/2)/2
        and repeat the process starting back at Step #2
4b. if the egg does not break, then go the "halfway" point in the upper half the remaing building: floor (n-(n/2))/2
        and repeat the process starting back at Step #2
5. Keep repeating the process until you can identify no more floors to move to.  The optimal floor is the last identified floor
        for which a dropped egg remained unbroken

Since this very similar to a binary search, the runtime complexity would be close to an O(log n) type of operation.

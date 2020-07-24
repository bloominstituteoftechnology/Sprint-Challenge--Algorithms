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

total floor = n
total eggs = t

start from mid-floor of buiding f (n/2):
  if egg breaks, move down to mid-floor of remaining n/2 = n/4 (decrease floor size -- small number -> move left in binary tree)
  if egg is unbroken, move  floor up of remaining n/2 = n/4 to find where it first breaks ( -> move right in binary tree)

This algorithm takes time complexity of O(logn) because this function implement binary search method.
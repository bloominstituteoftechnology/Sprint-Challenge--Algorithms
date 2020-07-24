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

### Minimizing how many eggs are broken:

Start on the first floor
Drop an egg
  If it breaks:
    this is the floor
  If it doesn't break:
    go up one floor
  If this is the top floor:
    no floor breaks the egg

### Minimizing how many eggs are dropped

Start in the middle floor
Drop an egg
  If it breaks:
    All floors above this will also break it
    If the floor below this one doesn't break the egg:
      this is the floor
    Go to the floor between this floor and the bottom and repeat the loop
  If it doesn't break:
    All floors below this will also break it
    If the floor above this one breaks the egg:
      the floor above this floor is the floor
    Go to the floor between this floor and the top and repeat the loop
If the loop doesn't return anything no floor breaks the egg
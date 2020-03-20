# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
    
    n = 1
    first pass
    a = 0 + 1 * 1
    a = 1

    a < 1 cubed

    second pass
    a = 1 + 1 * 1
    a = 2

    a > 1 cubed O(n^n+1)

    n = 2
    first pass
    a = 0 + 2 * 2
    a = 4

    a < 8 

    second pass
    a = 4 + 2 * 2
    a = 8

    a = 2 cubed

    third pass

    a = 8 + 2 * 2
    a = 12

    a > 2 cubed


    n = 5
    first pass
    a = 0 + 5 * 5
    a = 25

    a < 5 cubed

    second pass
    a = 25 + 5 * 5
    a = 50

    a < 5 cubed

    third pass
    a = 50 + 5 * 5
    a = 75

    a < 5 cubed

    fourth pass
    a = 75 + 5 * 5
    a = 100

    a < 5 cubed

    fifth pass
    a = 100 + 5 * 5
    a = 125

    a < 5 cubed

    sixth pass
    a = 125 + 5 * 5
    a = 150

    a > 5 cubed

    
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

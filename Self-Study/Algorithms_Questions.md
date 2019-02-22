# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n)           #O(n)
      a = a + n * n
```

```
b)  sum = 0                         #O(n^3)
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```

```
c)  bunnyEars = function(bunnies) { O(n)
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.



----------------------------------------------------------

Big O === 0(n)

def eggnary_search(floors, egg, humpty_dumpty):
  #humpty_dumpty == minimum egg_break limit == floors[25]
  if len(floors) == 0:
    return -1 # array empty
  
  low = 0
  high = len(floors)-1
  
  while low <= high:
    middle = (low+high)//2
    if floors[middle] > humpty_dumpty:
      egg = egg - 1
      high = middle - 1
    elif floors[middle] < humpty_dumpty:
      high = middle + 1
    else:
      return middle
  return -1 # not broken

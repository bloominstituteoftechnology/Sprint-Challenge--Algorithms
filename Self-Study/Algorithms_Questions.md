# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n)  O(n^2)
      a = a + n * n
```

```
b)  sum = 0 O(n^4)
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```

```
c)  bunnyEars = function(bunnies) { O(undefined)
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

def broken_eggs(n, f):
  while f in range(10:):
    saving_eggs(n, f)
    broken_eggs(n - 1, f)
    if n == 0:
    return "You Have Broken All Yo Eggs"

def saving_eggs(n, f):
  f = num_of_floors
  n = num_of_eggs
  for i in range(num_of_floors):
    if num_of_eggs == num_of_eggs - 1:
      return ("Break starting point", num_of_floors)

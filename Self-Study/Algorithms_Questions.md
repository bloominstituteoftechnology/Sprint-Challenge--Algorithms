# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n)   O(n) 0 < 2 * 2 * 2 = 0 < 8
      a = a + n * n |       a = 0 + 2 * 2 = 4 | a = 4 + 2 * 2 = 8
```

```
b)  sum = 0
    for (i = 0; i < n; i++)                 O(n)
      for (j = i + 1; j < n; j++)           O(n+1)
        for (k = j + 1; k < n; k++)         O(n+2)
          for (l = k + 1; l < 10 + k; l++)  O(n+3)
            sum++ O(1)
```

```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)   O(n)
    }
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

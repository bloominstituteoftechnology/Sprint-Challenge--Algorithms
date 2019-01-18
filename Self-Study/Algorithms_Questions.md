# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0                  # O(1)
    while (a < n * n * n)  # O(3n) => O(n)
      a = a + n * n        # O(1)

    # O(1) * O(n) * O(1) = O(n)
```

```
b)  sum = 0                                          # O(1)
    for (i = 0; i < n; i++)                          # O(n)
      for (j = i + 1; j < n; j++)                    # O(n)
        for (k = j + 1; k < n; k++)                  # O(n)
          for (l = k + 1; l < 10 + k; l++)           # O(1)
            sum++                                    # O(1)

    # O(1) * O(n) * O(n)* O(n)* O(1)* O(1) = O(n^3)
```

```
c)  bunnyEars = function(bunnies) { 
      if (bunnies == 0) return 0 
      return 2 + bunnyEars(bunnies-1)
    }

    # only one pattern that calls itself = O(n)
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

_n_ = stories
_f_ = floor
_n_ >= _f_  # eggs breaks
_n_ < _f_   # eggs don't break


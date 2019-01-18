# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:
```
O(n) <- n is constant, so the time it takes to reach the condition remains constant
a)  a = 0 O(1)
    while (a < n * n * n) O(n)
      a = a + n * n O(1)
```

```
O(n) * O(n) * O(n) * O(n) = O(n^4)
b)  sum = 0 O(1)
    for (i = 0; i < n; i++) O(n)
      for (j = i + 1; j < n; j++) O(n) <- No matter if index increases n will remain constant.
        for (k = j + 1; k < n; k++) O(n)
          for (l = k + 1; l < 10 + k; l++) O(n)
            sum++ O(1)
```

``` 
   O(n) * O(1) = O(n)
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0 O(1)
      return 2 + bunnyEars(bunnies-1) O(n)
    }
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.
The easiest way to reach that value is by doing the following steps:
1) Take the mid point of the number of stairs
2) If the egg breaks take the list of numbers below the midpoint, if it doesn't take values under the midpoint
3) Repeat those two steps with the new list until you find the value of f
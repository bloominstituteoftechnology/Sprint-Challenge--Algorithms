# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0 // n = 5, 10
    while (a < n * n * n): // 0 < 125, 25 < 125, 50 < 125, 75 < 125, 100 < 125, 0 < 1000
      a = a + n * n // a = 25, 50, 75, 100, 125 a = 100, 200, 300, ..., 1000: n times
```

```
b)  sum = 0 // n = 10
    for i in range(n): // 0, ..., 9: 9 times, (n)
      i += 1 // 1, ..., 10
      for j in range(i + 1, n): // 2, 3, ..., 9: 9 - 2 = 7 times,  (n - 3)
        j += 1 // 3, 4, ..., 10
        for k in range(j + 1, n): // 4, 5, ..., 9: 9 - 4 = 5 times, (n/2)
          k += 1 // 5, 6, ..., 10
          for l in range(k + 1, 10 + k): // 6, 7, 8, ..., 15: 9 times
            l += 1 // 7, 8, 9, ...,16
            sum += 1 // 1, 2, 3, ..., 10
```

```
c)  def bunnyEars(bunnies): // bunnies = 10
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) // 2 + 9, 2 + 8, 2 + 7, ..., 2 + 0 = 10 times
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

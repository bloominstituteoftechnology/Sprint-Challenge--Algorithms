```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
 this code asks that while a < n cubed, a equals a plus n squared. that means that when n is 1, it will run once. when n is 2, it will run twice, when n is 3, it will run 3 times... you get where i'm going with this. O(n)
```
b)  sum = 0

    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1
```
This has three nested for loops. O(n^3).
```
c)  def bunnieEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
This function recursively passes bunnies to itself decremented by one every time. The base case will exit when bunnies equals zero. so it will run n times. O(n)

```
Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the
runtime complexity of your solution.
```

I would follow the procedure of a binary search - start at the middle floor, and drop my egg. If it breaks, I want something below me. If it doesn't I want something above me. Either way, I would move to the middle of that section and drop my egg. If it breaks, higher. If it doesn't lower. Eventually, I should be able to find the first floor that it breaks on.

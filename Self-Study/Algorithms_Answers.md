Add your answers to the Algorithms exercises here.

```
a)  a = 0
    while (a < n * n * n) 
      a = a + n * n
```
A) O(n) - Updating `a` inside of the loop is based on `n^2`, and our loop will continue until `a < n^3`. 
Because updating `a` is growing at `O(n^2)` and `a` is a constant, we get `O(1) + O(n^2)` which is `O(n^2)`.

`O(n^3) - O(n^2) = O(n^1) = O(n)`

_____
```
b)  sum = 0
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```
B) O(n^4) - There are four nested loops, each of which are dependent on `n`. 

____
```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```
C) O(n) - This is a recursive function that is based on the amount of `bunnies` passed in. It continues to recurse until the size of bunnies is zero.


```
Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.
```
I would use divide and conquer. Starting at the middle, I would see if the eggs broke, if they did, then everything higher than the middle will cause them to break as well. If they didn't, then I know I could drop them from higher. Recursively, we could continue this until we found the last floor in which they did not break. 
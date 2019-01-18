Add your answers to the Algorithms exercises here.

# Exercise 1

a) a = 0
while (a < n _ n _ n):
a = a + n \* n

--- A is a constant. The final product of this algo always returns a+n no matter the value of n....linear.
--- This is 0(n) run time.

b) sum = 0

    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1

c) def bunnieEars(bunnies):
if bunnies == 0:
return 0

      return 2 + bunnyEars(bunnies-1)

-- This is a O(n!) problem as we are recursively calling bunnieEars and decrementing each bunnie by one and then computing another pair of ears for the next bunny.

# Exercise 2

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

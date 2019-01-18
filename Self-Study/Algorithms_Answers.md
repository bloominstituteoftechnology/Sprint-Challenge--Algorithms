Add your answers to the Algorithms exercises here.

# Exercise 1

a) a = 0
while (a < n _ n _ n):
a = a + n \* n

A is a constant. The final product of this algo always returns an^2
This is 0(n^2) run time.

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

# Exercise 2

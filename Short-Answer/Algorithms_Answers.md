Add your answers to the Algorithms exercises here.

## Exercise I

a)  a = 0
    while (a < n * n * n):
      a = a + n * n

O(n). While it may be trying to trick you into thinking it's O(n^3) by referencing
n * n * n in the while loop, that has to be divided by the n * n in "a = a + n * n"

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

O(n^3). Each of the first three for loops runs on the order of n times. The fourth for
loop is unimportant.

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

O(n). Same as a factorial. bunnyEars gets called bunnies times.



Add your answers to the Algorithms exercises here.


```
a)  a = 0
    while (a < n * n * n):  # O(n)
      a = a + n * n
```
# O(n)

# The while loop takes the n input only runs n number of times.

```
b)  sum = 0

    for i in range(n):                      # O(n)
      i += 1
      for j in range(i + 1, n):             # O(n)
        j += 1
        for k in range(j + 1, n):           # O(n)
          k += 1
          for l in range(k + 1, 10 + k):    # no n 
            l += 1
            sum += 1
```

# b contains a nested loops. the n input is required for 3 of the 4 loops.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
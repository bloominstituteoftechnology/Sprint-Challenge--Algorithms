
## Exercise I

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
# O(n**3)

# n * n * n

# b contains a nested loops. the n input is required for 3 of the 4 loops. Loop one is loop one is needed to iterate for all 3 loops, loop two for itself and the inner loop, and loop 3 for itself.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

# O(n)

# the function is constant at the first return. the second return alters the value of bunnies, causing a loop to run bunnies number of times.

## Exercise II

    n = floors of our building

    # for every floor(f) in n
        # if f < brokeneggfloor:
            return True
        # return False

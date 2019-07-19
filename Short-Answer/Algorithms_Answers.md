Add your answers to the Algorithms exercises here.


```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```
b)
  sum = 0
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

```
c)  
  def bunnyEars(bunnies):
    if bunnies == 0:
      return 0

  return 2 + bunnyEars(bunnies-1)
```

a. linear - O(n)

b. exponential - O(2^n)

c. linear - O(n),
It prints 2 while recursively deincrimenting 


Exercise 2:
The Egg drop problem:

reduce the potential set of floors in half per drop with binary search!

Check at the middle, if breaks, check between bottom and middle, if survives check between middle and top.
the between value becoming the new middle

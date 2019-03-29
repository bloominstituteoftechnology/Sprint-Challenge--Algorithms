Add your answers to the Algorithms exercises here.

a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
this psuedo code basically says:
 for i iterations, keeping iterating while...
 i*n^2 < n^3 
which means, depending on the value n, this loop will need to iterate n times before completing,
 meaing the runtime complexity is n^1 (n of 1).
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
the base loop in this psuedo code iterates n times with 3 subsequent nest loops that run to a length of n.
that means this runtime should be n^4 (n is raised to a power for each loop of length n). since the 3rd loop
goes to length n (incrementing k by 1 each time) that means the 4th and final loop is also going for a length of n (10+k)

```

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

```
for an input value of 0 or -1 or any odd -negative number this loop will eventually return a value of 0.

for any other values this loop will loop infinitely because it decrements by 1 and increments by 2 on each
iteration.

therefore this should have infinite runtime
```

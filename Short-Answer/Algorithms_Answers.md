#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This snipet initially looks like a O(n**3) runtime, but because the a value inializes at a value of n * n and then increments by n * n for each iteration of the while loop, it is actually O(n) runtime because it is basically n * n * n == n * (n * n) or n * a == n * a.

```python
    a = 0
    while (a < n * n * n):
      a = a + n * n
```


b) This bad boy is O(n log n) because we have the for loop (n) then a while j < n, this while loop will not equal n because j increments exponentially, but it is a function of n so we'll call it a log n complexity.

```
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

c) O(n), the function is being called recursively n times so it is linear.

```
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II



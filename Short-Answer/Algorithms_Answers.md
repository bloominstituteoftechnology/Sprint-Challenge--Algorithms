#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - while loop

```a = 0
while (a < n * n * n):
    a = a + n * n
```

b) O(n ^ 2) - nested loops

```
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

c) O(n) - because it is recursively calling the function

````
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II
````

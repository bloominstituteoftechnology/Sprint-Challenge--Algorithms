#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

```python
    a = 0
    while (a < n * n * n):
      a = a + n * n
```

a) This algorithm is an O(n). This code will run once no matter what the size of n is and will only repeat once the while loop starts up. This is linear and does not get modified.

from TK:
O(n) As the size of the input increases, the runtime or space used is will grow at the same rate

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

So with this algorithm, there is a nested loop so therefore O(n) gets multiplied by itself which is O(n^2)

Google:
O(N2) represents an algorithm whose performance is directly proportional to the square of the size of the input data set. This is common with algorithms that involve nested iterations over the data set.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

This algorithm is O(n) because recursion is being used and it will run and run until the end, but we do not know how many bunnies or how many times it needs to run.

from TK:
O(n) As the size of the input increases, the runtime or space used is will grow at the same rate

## Exercise II

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

```
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

```

## Exercise II

```
The simplest answer would be to actually iterate over each floor, starting from the lowest floor and dropping the eggs until it breaks and so forth - however we don't know what the first floor is and this would also result in the worst-case scenario for runtime-complexity as well.

I think the best solution would be to get the range of the building (aka number of floors) and start at the middle. We can then throw an egg
at len(n) / 2 and if it breaks, we do a while loop to go down the floors, if it doesn't break, we go up a floor. This way we are able to minimize the throws. Chunking into thirds or fourths seems like a viable option too, but it just enhances the complexity and the range in which the egg actually breaks, potentially making the number of broken eggs much larger than needed.

Starting from the middle of the building, in the worts case scenerario, the biggest number of eggs that can be broken is len(n / 2) - 1.

This operation has a runtime of O(n), but if we perform a binary search as we search the floors, it can be optimized to a O(log 2n) runtime complexity.

```

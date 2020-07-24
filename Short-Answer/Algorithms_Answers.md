#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

```
# constant O(1)
a = 0
    # O(n^3)
    while (a < n * n * n):
      # n^2
      a = a + n * n
```
Because the while loop runs while a is less than n^3 and then a increases by n^2, we can 
say that the runtime complexity is O(n^3)/O(n^2) = O(n)

The time complexity is O(1) + O(n^3) / O(n^2) = 

`O(n)`

b)


```
# constant O(1)
sum = 0
    # linear O(n)
    for i in range(n):
      # constant O(1)
      j = 1
      # ogarithmic Log(n) because j doubles each iteration
      while j < n:
        # constant O(1)
        j *= 2
        # constant O(1)
        sum += 1
```
The time complexity is O(1) + O(n) * (O(1) * O(log n) * O(1 + 1) = 

`O(n log n)`


c)

```
def bunnyEars(bunnies):
      # constant
      if bunnies == 0:
        return 0

      # O(n)
      return 2 + bunnyEars(bunnies-1)
```

The time complexity is = 

`O(n)`

The number of times bunnyEars runs is directly proportional to the amount of bunnies popped in. This is the same exact heckin thing as putting 

```
def bunnyEars(bunnies)
    return bunnies * 2
```
which would be constant instead of linear

## Exercise II

Heyyy we shouldn't normalize food waste but ok here's what I would do:

I would take a look at how high the building is, and go to the middle floor.

I would then drop an egg.

If the egg broke, I would want to go down. If it didn't break, I would want to go up.

I would calculate how much I would want to go down or up based on how much of the building I haven't seen and by cutting that in half each time.

I would continue on this process over and over again until finding the correct value of f.

This is exactly like binary search and has a runtime complexity  of O(log n)

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime is O(1+n*1) == O(n)

```
a = 0   # O(1)
while (a < n * n * n): # O(n)
    a = a + n * n   # O(1)
```

The control variable `a` increases everytime with `n^2`.
But the while loop checks if the `a < n^3`.
Basically it checks `n^2 < n^3` which gives a complexity of `O(n)`.

b)  O(1+n*(1+log(n)*(1+1))) == O(nlog(n))

```
sum = 0             # O(1)
for i in range(n):  # O(n)
    j = 1           # O(1)
    while j < n:    # O(log n)
        j *= 2      # O(1)
        sum += 1    # O(1)
```
`while j < n` has O(log n) complexity because the control variable `j` is alway multiplied by 2

c)  O(1+1+n) == O(n)

```
def bunnyEars(bunnies):
    if bunnies == 0:                # O(1)
        return 0                    # O(1)

    return 2 + bunnyEars(bunnies-1) # O(n)
```

The function will recurse n times until n=0.

## Exercise II

```
# Base case:
# Start on the ground  floor
# Get the middle floor between the start point and the top floor (n)
# run until floor f:
    # drop the egg
    # if the egg breaks:
        # move to the middle point between current location and the ground
    # otherwise:
        # move to the middle point between current location and the top floor
# return floor f
# floor f is the highest floor where the egg doesn't break
```

This approach is similat to a binary search, so the runtime complexity is O(log n)

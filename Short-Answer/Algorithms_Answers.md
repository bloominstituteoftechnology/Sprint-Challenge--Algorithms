#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) **O(n)** - The while loop runs as long as `a` is smaller than `n^3`. But as `a` increases with `n^2` with each loop, the runtime is `n^3` divided by `n^2`, i.e. `n` times.


b) **O(n log n)** - The outer for loop runs `n` times. For each run of the outer loop, the inner while loop runs `log n` times (base 2, as `j` is doubled in each run of the inner loop). Multiplying runtimes, this code will run `n log n` times.


c) **O(n)** - This function recursively calls itself `n` (bunnies) times. We can ignore constants.

## Exercise II

My suggestion would be to use a BST-like algorithm with runtime `O(log n)`. Pseudocode would look something like this:

```py
def egg_floor(low, high):
    if low < hig:
        floor = (low + high) // 2
        if 'egg breaks':
            return egg_floor(low, floor-1)
        elif:
            return egg_floor(floor+1, high)
        else:
            return floor
```
#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
`O(n^3)`
as `n` increases in value, this snippet will grow exponentially. the while loop determines how many times the algorithm will run and has the formula `n * n * n` which is the same as `n^3`



b)
`O(n log(n))`
as `n` increases, it linearly increases the outer for loop (`for i in range(n)`), but the inner while loop `while j < n` runs roughly log(n) times as doubling `j` is very similar to halving `n`

c)
`O(n)` (or `O(bunnies)`, technically)
for each additional bunny, the the algorithm runs one additional time, scaling linearly

## Exercise II

The real answer is the following "algorithm"
`return 0`
Why? There's no constraint on the question asking for `f` to be maximized, and 0 is the lowest positive integer value, so you can't get lower than that to drop your eggs. Therefore, we've minimized the number of dropped + broken eggs to 0. The time complexity of this is `O(1)` as the algorithm doesn't change via the size of the input.

However, if the intention behind the question was ultimately to find the highest value of `f` while also retaining the previous constraints...

```
def eggDropBreaks(floor):
    # drop an egg
    # if it breaks, return True
    # else return False

def findHighestNonBreakFloor():
    # set f to 0
    # loop over the following
        # drop an egg from current value of f
        # if it doesn't break
            # increment f by 1 and repeat the loop
        # else
            # return f - 1
```

the runtime complexity would be `O(n)` where `n = f` as the algorithm will scale linearly (grow by one iteration) as `f` increases.

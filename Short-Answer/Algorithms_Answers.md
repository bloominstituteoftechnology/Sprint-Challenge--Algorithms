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



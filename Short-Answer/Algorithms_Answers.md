#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This loop is `O(n)`. My reasoning is that, although it looking for `a` to be
greater than `n^3`, `a` increases by `n^2` each iteration. Dividing `n^3` by
`n^2` leaves us with just `n`.


b) This algorithm has a runtime of `O(n log n)`. The outer goes from 0 to `n`,
which means it is `O(n)`. The inner loop starts at 1 and then doubles until it
is greater than `n`. Doubling each time means that the loop will complete in
`O(log2 n)` time. And because they are nested loops the time complexity is
multiplied, giving us `O(n log n)`.


c) This algorithm is `O(n)`. This is because it recursively calls itself. Each
call subtracts a constant amount (in this case 1), bringing it one step closer
to the base case of 0. Because it is a constant amount and there is only one
recursive call each time, the number of steps is a linear function based on
the input.

## Exercise II



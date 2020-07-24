#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

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
recursive call each time, the number of steps is a linear function based on the
input.

## Exercise II

This is a case where binary search is applicable. To understand why, let's
review the similarities.

1. We have an 'array' of elements, in this case the floors of a building
2. We have a function for comparing each element. When we drop the egg, an in
   tact egg tells us that we are too low, and a broken egg tells us we are too
   high.

With the 2 properties of the problem in mind, let's write out an algorithm.

1. Note the lowest floor that an egg has been broken after dropping
2. Note the highest floor that an egg has been in tact after dropping
3. Go to the floor exactly in the middle of those two floors
4. Drop the egg
5. Note the floor and whether the egg broke or not
6. If the lowest broken egg floor and the highest in tact egg floor are next to
   each other, stop. The lowest broken egg floor is `f`.

The runtime of this algorithm is `O(log n)`. Binary search is `O(log n)` because
at each step it halves the amount of elements it has to search, giving us a nice
logorithmic curve as the number of floors increases.

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `O(n)`

The while loop runs until `a` reaches `n * n * n` which makes the while loops time complexity a `O(n^3)`. Everytime the loop runs, `a = a+ n^2` is executed. This makes this a time complexity `O(n^2)`. Now if we take `O(n^3)` and subtract `O(n^2)`, we'll get `O(n)`.


b) `O(n log n)`

For the initial `for loop` we iterate over the `range(n)`, which gives us a time complexity of `O(n)`. Then inside the `for loop`, we have an additional while loop which checks if the value of j has reached `n`. We then multiply j by 2. This gives the while loop a time complexity of `O(log(n))`. Now combine these two time complexities and we will get `O(n log n)`.


c) `O(n)` 

Question c is a recursive method that runs as many times as the input because it is being decremented by 1 in each recursive call.

## Exercise II

First thing we need to do is find the midpoint. If the egg breaks, we need to check if the egg breaks the same way using only the lower half of the floors remaining.
if the egg doesn't break, we need to check the same way with the upper half discarding the lower half.
Then continue to recurse until we are left with two floors(which will be our base case), lower half should not break, upper half should break.

`O(n log n)`


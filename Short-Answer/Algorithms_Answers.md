#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity is `O(n^3)`. The `while` loop runs depending on how big `n^3` is. The code will take exponentially longer to run the igger `n` is.

b) Runtime complexity is `O(n)`. The bigger `n` is the longer the code will take to run in a linear scale.


c) Runtime complexity is `O(1)`. The function only checks whether or not bunnies exists. The amount of bunnies does not change how long it takes to run.

## Exercise II

Since `f` is unknown, and each floor is on top of the other (therefore sorted), we can use `binary search` to determine which floor `f` corresponds to while breaking the least amount of eggs.

Runtime complexities:
- Best case scenario: `O(1)`
- Worst case scenario: `O(log n)`
- Average case: `O(log n)`


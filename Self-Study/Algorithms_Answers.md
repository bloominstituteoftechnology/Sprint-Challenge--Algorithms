Add your answers to the Algorithms exercises here.

a) `O(n)`

- This function has two constant operations `O(1)` and one looping operation
  based on the value `n` `O(n)`. `O(n)` therefore is the dominant operation
  contributing to complexity.

b) `O(n^4)`

- This function has one constant operation `O(n)`, and 4 nested loops that
  depend on `n`. Each nested loop becomes an increases `n` to the power.
  This function will scale in operations `n` to the power of 4

c) `O(n)`

- This function is recursive and runs once each time, for the size of `n`.
  Just like a single loop this translates to `O(n)`

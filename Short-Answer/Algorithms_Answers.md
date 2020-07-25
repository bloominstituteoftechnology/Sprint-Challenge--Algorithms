#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
n X n X n results to O(n^3)
The computation affects the while loop
in that a has to be incremented in each pass.

b) O(n _ (1 + (log n))) = O(n _ log n) = O(n log n)
This is 2 parts . The first part is i in range has to
go through whatever the value of (n) and that is tied to
the size of (n). J is O(1). Then there is the inner while
loop that happens for each item in n. At each pass it is
doubling the size of j. This double the size of the incrementer
making it O(log n).

c) O(n)
This is a recursive call and it relies on the input.

## Exercise II

n story building.
plenty of eggs.
floor f or higher eggs get broken.
less than f eggs does not get broken.
find the value of f such that it minimize drop eggs and broken eggs.

Binary Search

if floor > f eggs is broken
n floor/ 2 and countinue sorting by half
loop until there are only 2 floors.

This will result in O(n) since it uses Binary Search.

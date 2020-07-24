#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)  You have n^3 in the while loop and n^2 in the condition check. 


b) You have nested loops.  Big O is O(n^2)


c) O(n)  We're using recursion, but this is linear complexity for Big O

## Exercise II

So, we have an ordered list (floors) which means we can use a Binary Search which has O(log N) complexity.

Essentially, start at the middle floor.

Drop the egg.

If the egg breaks, move to the middle of the bottom half.  

Change the top floor (or end) in our comparison list to middle - 1 floor.

If the egg doesn't break, move to the middle of the top half.

Change our beginning to the middle + 1.

Keep repeating the process until we've found our result which is when the egg breaks at floor + 1 (one floor higher), but not from current floor.





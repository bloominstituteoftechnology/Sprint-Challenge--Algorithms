#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The termination of the `while` loop is essentially n cubed and the
value being compared is a multiple of n squared.  As n grows, the while
loop will complete when it is executed n times.

I would say the run time grows at the rate of n.  Or O(n).  The `while`
loop looks scary but the entire operation should complete in a reasonable
amount of time.

b) In this snippet, the outer `for` loop iterates `n` times.
The inner while loop will iterate more slowly as the termination
variable j doubles with each `while` loop execution.  

This snippet looks close to an O(n log n) type of run time due to 
nature of the doubling of j with each pass of the inner `while` loop.


c) This snippet is a recursive function but it appears to to call
itself `n` (or bunnies) times.  Essentially the function recurses
by decrementing n (bunnies) by 1 until n decrements down to 0.

This looks like O(n) type of execution in terms of time.

## Exercise II



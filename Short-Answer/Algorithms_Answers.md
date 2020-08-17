#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n).  The algorithm will run n times until it is higher than the conditional loop.


b) O(n*log(n)). This algorithm has nested for loops.  The inner loop has a log(n) complexity, because j doubles each time. The outer loop will run n times.


c) O(n). The function is recursive, and will run n times.

## Exercise II

The quickest way to determine f is by dropping the egg from halfway up the building, or at floor n/2 (a = n/2).  If the egg breaks, the chosen floor is either correct or too high, so you pick halfway between all the lower floors (b = a/2).  If the egg doesn't break, then f is higher than the floor you chose, so the next floor you should pick is halfway between the top and a (b = a + (a/2)). You continue to drop eggs at the halfway mark of the untested area until you get a broken egg at a floor directly above a floor where the egg does not break.

The runtime complexity is log(n).

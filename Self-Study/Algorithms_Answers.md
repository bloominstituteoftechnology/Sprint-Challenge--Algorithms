Add your answers to the Algorithms exercises here.

## Exercise I

a. O(n) this loop is only running linearly based on n. If n == 1 the loop is going to run 1 time. If the n is 2 it's going to run 2 times. If n is 3 it's going to run 3 times, etc.

b. O(n^4) This example has four loops each one nested inside of the next. Each loop alone is O(n). So multiplying those: O(n) _ O(n) _ O(n) \* O(n) = O(n^4).

c. O(n) This is a recursive function that is running just like a loop. Because it's decrementing by one each time it's called, it is looping through all of the inputs.

Add your answers to the Algorithms exercises here.

## Exercise I

a. O(n) this loop is only running linearly based on n. If n == 1 the loop is going to run 1 time. If the n is 2 it's going to run 2 times. If n is 3 it's going to run 3 times, etc.

b. O(n^4) This example has four loops each one nested inside of the next. Each loop alone is O(n). So multiplying those: O(n) _ O(n) _ O(n) \* O(n) = O(n^4).

c. O(n) This is a recursive function that is running just like a loop. Because it's decrementing by one each time it's called, it is looping through all of the inputs.

## Exercise II

The best way to find the value of _f_ would be to use `binary search`. Since we know that a storied building is already sorted by stories we can find _f_. To do this we would find the middle floor by determining the height of the building in stories divided by 2. If it is _f_ we are done. If _f_ is lower than the middle floor selected we can rule out the top half of floors. And vice versa... if it is higher than the middle index. We can then repeat these steps on loop until _f_ is middle element. We can then figure out how many floors are below it. `Binary Search` is O(log n).

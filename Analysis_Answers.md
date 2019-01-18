Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   - Heap insert: `O(log n)`
   - Heap delete: `O(log n)`
   - Heap get max: `O(1)`

## Runtime complexity is O(n \* log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

I don't think the time complexity of my algorithm can get better than O(n _ log n). Using the heap class algorithms gives a time complexity of log n, but we still need to run it on each element of the array (n). Which gives O(n _ log n)

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

I believe the space complexity is O(n). I'm not increasing the stack at all, but we did introduce a new variable and add n variables to it. To make it O(1) we would need to sort the original array.

Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   #O(n log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
    I don't think it is possible since we have to loop through our array at least once with the current functions. I would need a different heap running in-place functions.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)
   The space complexity is 0(n)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
    We would have to drop the i in range function and do recursion instead. We would also need a different heap sort, and perform operations in-place.
Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   O( 2 log(n) )

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   No

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   - The space complexity for my heapsort function is O(n) because a new list is being created and returned to store the new sorted values. In order to achieve O(n) space complexity, the values would need to be swapped in place inside of the original list which eliminates the need to create a new list to store the sorted values.
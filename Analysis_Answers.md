Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   A: O(n^2)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   A: Yes, I could figure out how to use the methods in the Heap class, which have O(log n) time complexity.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   A: It is O(n) space complexity due to a new list being created in order to return the sorted list. To get to O(1) we would have to sort the values within the 'arr' list that is the input without copying it over to a new list, and returning the sorted 'arr' list.
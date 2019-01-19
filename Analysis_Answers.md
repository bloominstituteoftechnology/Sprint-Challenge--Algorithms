Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   # Heap is O(n log n) since we loop through each el in array and apply it to the Heap .insert
   # O(n log n)          =                           O(n)       *             O(log)
2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   # Timsort or another method that evaluated how orderly the array was to begin with could improve run time
   # But otherwise, heap sort is similar in run time to mergesort

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   # Mine is O(n) since there is each sorted item is going into a final sorted to be returned
   # One could a method for sorting the original array in place by swapping it
   # with the desired sorted value. So, that the space complexity
   # is O(1). So that the array decreases
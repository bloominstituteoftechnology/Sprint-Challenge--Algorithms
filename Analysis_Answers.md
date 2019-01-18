Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   O(n3 log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   I do not believe so. The class would have to be modified. The loop for inserting
   the arr is necessary. The while loop to check if the heap size is larger than 0 is
   also needed, since we need to know to delete from the heap and insert the storage
   into the result array.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   O(2) since heapsort uses the method's storage, and result array.
   Transfering the sort array directly to the answer array could remedy this.
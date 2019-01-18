Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

    Answer:
    When we first build the heap by inserting each item in the array we 
    perform an O(n) operation. When we then get the max value, and 
    delete it from the heap we perform a O(1 * log n) operation. 
    Overall we have the following operation: O( n log n).

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

    Answer:
    We need to build the heap by making a full loop at least once. Since 
    delete seems to be O(log n) we will not be able to make it more 
    efficient than O(n log n)

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
   
   Answer:
   Since my solution saves a result array and then returns that, the
   space complexity of my solution is O(n) since space increases with the 
   size of the input. In order to reduce it to O(1) we would have to 
   remove the result array and only use the Heap's storage as the return
   value.
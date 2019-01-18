Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`
   
   ==> The runtime complexity of the heapsort() is O(n log(n)).

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   
   ==> Well, if we don't do the two for-loops, we might get better time, but i'm not sure how. Maybe we can turn the array into a heap directly and not use the Heap class?

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
   
   ==> Space complexity is going to be O(n) since we need the same amount of space as the input array to use in the heap. However, we don't need any extra space since we are reusing the input array for the output.
      If we want the O(1) space complexity, we would need to turn the input array into a heap directly and sort it in place as well.

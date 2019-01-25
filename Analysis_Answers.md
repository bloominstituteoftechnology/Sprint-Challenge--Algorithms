Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   - Heap insert: `O(log n)`
   - Heap delete: `O(log n)`
   - Heap get max: `O(1)`

I would say O(n^) because O(log n) + O(log n) = O(n) and O(n) + 0(1) would just be O(n) because you drop constants, and I used insert which has a time complexity of O(n) so O(n) + O(n) = O(n^)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

Maybe by using something faster than the built in insert method

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   I think my heapsort would be O(n^) because I am making a copy of the array passed into the heap

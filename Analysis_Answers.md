Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   A: O(n) is the dominate runtime because it loops through a list every run.

   Other hints, to save you some searching:

   - Heap insert: `O(log n)`
   - Heap delete: `O(log n)`
   - Heap get max: `O(1)`
   - insert: `O(n)`
   - for loop: `O(n)`
   - while loop: `O(n)`

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   A: I don't believe I could get my algorithm to run in better time because the function still needs to loop through the entire array at least once.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   A: My heapsort function is O(n) because it allocates space to a new empty array. In order to get the space complexity to be O(1), I would have to do all modifications to the input array.

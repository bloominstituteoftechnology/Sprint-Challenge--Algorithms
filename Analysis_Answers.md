Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`
## Answer: 
O(log n), each sub function called was O(log n) and nothing was nested

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
## Answer: 
Yes, at least slightly because if I had used the get max function instead of delete in my second for loop, I would have shaved off a little run time. 


3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

## Answer: 
I believe my space complexity would be O(n) because of the new array I create and return for the sorted data. 

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
   ## Answer: 
   I think I could do the heapsort within the heap itself via new_heap.storage and this would bring it to O(1).
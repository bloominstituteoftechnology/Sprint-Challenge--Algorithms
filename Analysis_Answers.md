Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`
   Built in functions / my functions:
   * for loops:    `O(n)` *2
   * reversed:     `O(n)`
   O(log n) + O(log n) + O(1) + O(n) + O(n)
   2(O(log n)) + 2(O(n)) + O(1)
   O(log 2n) + O(2n) + O(1)
   take away constants and combine
   O(n log(n)) I think you would get rid of O(1)
   
2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   I think that I could make my algorithm run in better time by getting rid of the 
   first for loop that inserts all my data, and instead spread it in somehow. Basically
   getting rid of a for loop.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)
   
   The space complexity of my algorithm would be O(1) because I am not increasing the 
   stack or new variables depending on the size of the array it remains constant
   no matter what is passed through the function

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
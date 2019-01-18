Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   `For my solution as I am using `
           `Heap insert: O(log n)`
           `Heap delete: O(log n) to build hearsort()`
           `Two for loops of O(n) compexity to go through all list item while inserting into Heap() and for getting max from heap`
           `O(n) + O(log n) + O(n) + O(log n)`
           `Time complexity will be O(n log n)` 

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   `really as of now the knowledge and practise don't know the answer.`

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   `here the space complexity is O(n) as new heap is getting created. To have O(1) space complexity the sorting should be in place`

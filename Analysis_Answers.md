Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`
   
   O(n log n)
   * breakdown in `heap.py`

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   
   I don't think so. I cut down on some time complexity by reversing the order of the list at the end (O(n)) instead of inserting each item at index 0 (O(n) each time).

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)
   
   My heapsort implementation creates a result array that will take as much space as the original list passed in. It also creates a Heap which creates a storage class. This would be O(2n) but dropping the constant makes it O(n).

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
   
   The best optimization I can think of right now is to modify the Heap class so it takes the original list and sorts the smallest at the top. Then uses the delete func on the Heap instance O(log n), and regularly appends it to the end of the list O(1). Then to sort the rest, you would have to keep track of how many have already been sorted and then bubble_up the smallest number and do the same thing for the ones that come before. The Heap class may have to be additionally modified to ignore the already sorted indices while bubbling up.
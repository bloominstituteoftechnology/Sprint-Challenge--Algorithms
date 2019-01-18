Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   - Heap insert: `O(log n)`
   - Heap delete: `O(log n)`
   - Heap get max: `O(1)`

i believe my heap sort algorithm is O(n^2) because we have two loops that are both O(n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

using heap insert would definetly speed up our heapsort because the isnert does its own sorting which is log n versus our heapsort which is n^2

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

our heapsort i believe is O(N) space complexity because it creates a whole new list from the old array we passed in. If we wanted to get to O(1) we would need to sort on the original list that is passed in instead of appending to a new list.

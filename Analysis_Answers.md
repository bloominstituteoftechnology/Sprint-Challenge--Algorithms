Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

Answer: 
The time complexity of my heapsort is O(n log (n)^2). 

Components: 

* Initial for loop: (O(n)) 
* The Heap insert nested within the for loop: O(log n)
* The while loop: (O(n))
* The Heap delete nested within the while loop: O(log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
Theoretically, I could make it run more efficiently if I found a way to complete the Heap insert and Heap delete functionality with functions that run at (O(n)). This is because those functions are completed one after the other, rather than nested within eachother, so the multiple (O(n)) functions would still net a total time complexity of (O(n)).


3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new list with the sorted data. (Also remember
   that the size of the input list passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?


  Answer: The space complexity is (O(n)), because the number of heapResults we need to add scales linearly with the size of the list we input to the heapsort function. Getting it to have a space complexity of O(1) would require sorting the list in place, without creating a new list.
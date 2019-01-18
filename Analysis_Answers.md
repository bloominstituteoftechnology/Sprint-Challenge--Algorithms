Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

# In my heapsort function I have nested two O(n log n) due to the for loops and a O(n) due to the reverse built-in function. O(n log n) has the steeper curve, making my heapsort function O(n log n).

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
# According the the Big O cheat sheet, yes. My current function is considered average. However, looking at my code I'm not sure what changes I could make since I need the for loops to go through item on the list. One thing that I can change is to remove the reverse built-in function on line 31, and have the list be built in ascending order in the second for loop that way I don't need to reverse after the list is already created. Even if I am able to change this, it won't change the fact that the runtime complexity will still be O(n log n).

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
# To make my heapsort function into O(1) I would have to remove my sorted_list because there is no need to store any data in there since the Heap class has one called storage which is useful when swapping items.
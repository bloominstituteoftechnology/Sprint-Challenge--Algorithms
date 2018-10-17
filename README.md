# Sprint Challenge: Data Structures and Algorithms

For the data structures portion of this sprint challenge, you'll be implementing a few functions that build off of some of the data structures you implemented in the first half of the week. Then you'll be analyzing the runtimes of these functions.

For the algorithms portion of the sprint challenge, you'll be answering the questions posed in the `Algorithms_Questions.md` file regarding runtime complexities and algorithmic paradigms.

## Data Structures

It is recommended that you allot about 2 hours for this portion of the sprint challenge. 

### Task 1. Implement Depth-First and Breadth-First Traversal on the Binary Search Tree Class 
Navigate into the `ex1` directory in the `data_structures` directory. Inside, you'll see the `binary-search-tree.py` file with a complete implementation of the binary search tree class. Your first task is to implement the methods `depth_first_for_each` and `breadth_first_for_each` on the `BinarySearchTree` class:

   * `depth_first_for_each(cb)` receives an anonymous function as a parameter. It should then execute the anonymous function on each node in the tree in [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) order. Your task is to implement the logic to traverse the tree in the desired order. Remember that the anonymous function is supplied by the caller of the method. All you have to do is ensure that the anonymous function is being called on each tree node in the desired order.
   
     *HINT*: In order to achieve depth-first order, you'll probably want to utilize a Stack data structure. 

   * `breadth_first_for_each(cb)` receives a callback function as a parameter. It should then execute the anonymous function on each node in the tree in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) order. Your task is to implement the logic to traverse the tree in the desired order. Remember that the anonymous function is supplied by the caller of the method. All you have to do is ensure that the anonymous function is being called on each tree node in the desired order.
   
     *HINT*: In order to achieve breadth-first order, you'll probably want to utilize a Queue data structure.

NOTE: In Python, anonymous functions are referred to as "lambda functions". When passing in an anonymous function as input to either `depth_first_for_each` or `breadth_first_for_each`, you'll want to define them as lambda functions. For more information on lambda functions, check out this documentation: [https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

Run `python test_binary_search_tree.py` to run the tests for these methods to ensure that your implementation is correct.

### Task 2. Implement Heapsort
Inside the `ex2` directory you'll find the `heap.py` file with a working implementation of the heap class. Your second task is to implement a sorting method called [heapsort](https://en.wikipedia.org/wiki/Heapsort) that uses the heap data structure in order to sort an array of numbers. Your `heapsort` function should return a new array containing all of the sorted data.

Run `python test_heap.py` to run the tests for your `heapsort` function to ensure that your implementation is correct.

### Task 3. Analyze some runtimes
Open up the `Data_Structures_Answers.md` file. This is where you'll jot down your answers for the runtimes of the functions you just implemented. Be sure to also answer any other questions posed in the `Data_Structures_Answers.md` file!

## Algorithms

It is recommended that you allot about 1 hour for this portion of the sprint challenge.

For the algorithms portion of the sprint challenge, you'll be answering questions posed in the `Algorithms_Questions.md` document inside the `algorithms` directory. Add your answers to the questions in the `Algorithms_Answers.md` file.

## Rubric

Each test in the Data Structures portion is worth 2 points for a total of 6.  
Each runtime analysis question in the Data Structures portion is worth 1 point for a total of 6.  
Each question in the Algorithms portion is worth 2 points for a total of 8. 

In order to earn a score of 3, you'll need to score at least 90%, or 18 / 20 total possible points.

In order to earn a score of 2, you'll need to score at least 70%, or 14 / 20 total possible points.

Anything lower earns you a score of 1. 
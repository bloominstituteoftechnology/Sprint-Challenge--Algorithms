# Sprint Challenge: Data Structures and Algorithms

In this week's Sprint you explored and implemented some classic algorithmic approaches and used them to solve novel problems. You also implemented some classic and fundamental data structures and learned about how to go about evaluating their respective runtimes and performance. This Sprint Challenge aims to assess your comfort with these topics through exercises that build on the data structures you implemented and the algorithmic intuition you've started to build up.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your Challenge score is a measure of your ability to work independently using the material covered throughout this sprint. You need to demonstrate proficiency in the concepts and objectives that were introduced and that you practiced in the preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your submitted work reflects your proficiency in the concepts and topics that were covered this week.

You have three hours to complete this Sprint Challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons) and it also helps your project manager to more thoroughly assess your work.

## Description

This Sprint Challenge is split into two separate parts: a data structures portion and an algorithms portion.

### Data Structures

It is recommended that you allot about 1 and a half hours for this portion of the Sprint Challenge. 

#### Task 1. Implement Depth-First or Breadth-First Traversal on the Binary Search Tree Class 

Navigate into the `ex1` directory in the `data_structures` directory. Inside, you'll see the `binary-search-tree.py` file with a complete implementation of the binary search tree class. Your first task is to implement either `depth_first_for_each` or `breadth_first_for_each` on the `BinarySearchTree` class:

   * `depth_first_for_each(cb)` receives an anonymous function as a parameter. It should then execute the anonymous function on each node in the tree in [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) order. Your task is to implement the logic to traverse the tree in depth-first in-order fashion (as opposed to pre-order or post-order). Note that the pseudocode showcased on the Wikipedia article traverses the tree in-order. 

   * Remember that the anonymous function is supplied by the caller of the method. All you have to do is ensure that the anonymous function is being called on each tree node in the desired order.
   
     _HINT_: In order to achieve depth-first order, you'll probably want to utilize a Stack data structure. 

     * Run `python test_depth_first_search.py` to test your depth-first search implementation.

   * `breadth_first_for_each(cb)` receives a callback function as a parameter. It should then execute the anonymous function on each node in the tree in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) order. Your task is to implement the logic to traverse the tree in left-to-right breadth-first fashion.
   
   * Remember that the anonymous function is supplied by the caller of the method. All you have to do is ensure that the anonymous function is being called on each tree node in the desired order.
   
     _HINT_: In order to achieve breadth-first order, you'll probably want to utilize a Queue data structure.

     * Run `python test_breadth_first_search.py` to test your breadth-first search implementation.

> Note that in Python, anonymous functions are referred to as "lambda functions". When passing in an anonymous function as input to either `depth_first_for_each` or `breadth_first_for_each`, you'll want to define them as lambda functions. For more information on lambda functions, check out this documentation: [https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

> Note that it is not your job to worry about what the callback function being passed in is doing. That is up to the user of your traversal method. All you care about when implementing the traversal method is to call the passed-in callback in either depth-first or breadth-first order, depending on which traversal method you're implementing. 

#### Task 2. Implement Heapsort

Inside the `ex2` directory you'll find the `heap.py` file with a working implementation of the heap class. Your second task is to implement a sorting method called [heapsort](https://en.wikipedia.org/wiki/Heapsort) that uses the heap data structure in order to sort an array of numbers. Your `heapsort` function should return a new list containing all of the sorted data.

Run `python test_heap.py` to run the tests for your `heapsort` function to ensure that your implementation is correct.

#### Task 3. Analyze some runtimes

Open up the `Data_Structures_Answers.md` file. This is where you'll jot down your answers for the runtimes of the functions you just implemented. If you implemented depth-first traversal, just answer the questions pertaining to the depth-first traversal algorithm. If you implemented breadth-first traversal, just answer the questions pertaining to breadth-first traversal. Make sure you answer the heapsort questions as well!

### Algorithms

It is recommended that you allot about 1 and a half hours for this portion of the sprint challenge.

For the algorithms portion of the sprint challenge, you'll be answering questions posed in the `Algorithms_Questions.md` document inside the `algorithms` directory. Write down your answer and also write down a justification for _why_ you put down that answer. This could net you some partial credit if your justification is sound but the answer you put down turns out to not be correct. Add your answers to the questions in the `Algorithms_Answers.md` file.

### Stretch Problems

Implement the other tree traversal algorithm that you didn't implement on the `BinarySearchTree` class. Run the appropriate test file to test your implementation's correctness. Then go back to the `Data_Structures_Answers.md` file and answer the time and space complexity questions pertaining to the traveral method you just implemented.
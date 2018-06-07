# Sprint Challenge: Data Structures and Algorithms

For this sprint challenge, you'll be implementing a few functions that build off of some of the data structures you implemented in the first half of the week. Then you'll be analyzing the runtimes of all of the data structure methods. 

For the algorithms portion of the sprint challenge, you'll be answering the questions posed in the `exercises.pdf` file regarding runtime complexities and algorithmic paradigms.

## Data Structures
Before getting started, run `npm install` in the root-level directory to install needed dependencies for testing.

### Task 1. Implement Depth-First and Breadth-First Traversal on the Binary Search Tree Class 
Navigate into the `data_structures` directory. Inside the `src` directory, you'll see the `binary-search-tree.js` file with the completed code for the binary search tree class. Your first task is to implement the methods `depthFirstForEach` and `breadthFirstForEach` on the `BinarySearchTree` class. Think about what data structures you'll need to use in order to achieve the desired order of each respective method:

   * `depthFirstForEach(cb)` receives a callback function as a parameter. This method iterates over the binary search tree in [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) order, applying the supplied callback function to each tree element in turn. 
   * `breadthFirstForEach(cb)` receives a callback function as a parameter. This method iterates over the binary search tree in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) order, applying the supplied callback function to each tree element in turn.

Run `npm test binary-search-tree` to run the tests for this function to ensure that your implementation is correct.

### Task 2. Implement Heapsort
Inside the `src` directory you'll also find the `heap.js` file with the completed code for the Heap class that you worked on. Your second task is to implement a sorting method called [heapsort](https://en.wikipedia.org/wiki/Heapsort) that uses the heap data structure in order to sort an array of numbers. Your `heapsort` function should return a new array containing all of the sorted data.

Run `npm test heap` to run the tests for your `heapsort` function to ensure that your implementation is correct.

### Task 3. Analyze some runtimes
Open up the `Data_Structures_Answers.md` file. This is where you'll jot down your answers for the runtimes of the functions you just implemented. Be sure to also answer any other questions posed in the `Answers.md` file!

## Algorithms
For the algorithms portion of the sprint challenge, you'll be answering questions posed in the `exercises.pdf` document inside the `algorithms` directory. Add your answers to the questions in the `Algorithms_Answers.md` file.
Add your answers to the Algorithms exercises here.

## Exercise I

a) O(n). The complexity of this code is linear since the number of iterations of the while-loop will be equal to the size of input. In other words, the steps required to complete the execution of this algorithm increase or decrease linearly with the number of inputs.

b) O(n^3) There are 3 loops with respect to the input n.

c) O(n). The complexity of this function is linear. We can see this just by testing the function with a range of numbers (for i in range(x)), the output increases linearly by 2.

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

####ANS
Start at the middle floor (cut the problem in half), if that doesn't work, hit every floor between the middle of the floor that didn't work below or above the floor that we started with. Divide the problem in half until the solution is reached. This gives us a O(log2__n__) runtime.

#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) 0(log n)

- The loop increases a by n^2 while comparing a to n^3, thus the n^2 operation would compute faster than the n^3 operation

b) 0(n log n)

- The for loop will run until n is finished computing. Inside the while loop, j is multiplied by 2 each time the loop runs decreasing the times it will increment the sum

c) 0(n)

- Outside of the recursive call the runtime in 0(1), and only adds to the stack until n = 0

## Exercise II

Solution:

- You could use a binary search algorithm that starts in the middle and evaluates each guess to see if it's either too low or too high.

- The binary search will also cancel out half of the options and leave you with the least amount of broken eggs

- The runtime of our algorithm would be 0(log n), since the algorithm reduces the number of guesses on each loop

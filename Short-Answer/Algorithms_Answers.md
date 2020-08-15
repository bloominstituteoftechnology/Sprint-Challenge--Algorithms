#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) constant time. Given a number input, the function is siply doing a math calculation, there are no loops or iterations, simply multiplication and assigning a variable to a number


b)linear time. This function creates an iteration and uses a for loop. This means that as n gets larger, then the function will take longer to run proportionally to the size of n


c)exponential time. this function leverages a recursion, therefore as the input size grows, the number of operations that the function does grows exponentially to the input 'n'. For instance, if the input is 1, the function runs through once, then again to hit the base case for the recursion, and as 'n' increases, the number of times the function runs goes up by a factor of 'n'

## Exercise II
I would use code similar to a binary search. 
First I would find the middle floor of the building, and throw an egg from that window and check to see if it is broken. If it is broken, then I would run the same test, but for the bottom half of the building, starting the the middle of the bottom half. If the egg was not broken, then I would move to the top half of the building and run the same test. This would repeat until the floor is found where the egg is broken if dropped, and if dropped from that floor-1 is not broken, then that floor-1 is returned.

The time complexity of this search is logarithmic time, since as the imput size(number of floors) gets larger, the program will run longer, but not in a directly proportional way to the imput size. Since we are only looking at half of the tree each time we run the function, the runtime is logarithmic.


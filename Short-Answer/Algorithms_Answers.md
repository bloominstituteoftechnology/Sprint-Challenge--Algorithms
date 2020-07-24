#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity of this function is O(n) because it is linearly dependent on n meaning
the runtime will grow linearly as the input data increases. 


b) The runtime complexity of this function is O(n log n). It consists of two parts the for loop and the while loop.
The leading n in O(n log n) comes from the for loop as it loops through the entire input. The log n comes from the while loop 
because as n increases the number of operations increases at a rate thats slower than linear. 


c) From what I can tell this function is O(n) because it starts from n and loops through each value of n subtracting 1 each time
until n = 0

## Exercise II


I'm sure there are better solutions but the most basic solution would be to loop through a range of n to 0 counting down.
Through each iteration we check to see if the current floor is f.
If the current floor is not f the loop goes to the floor below n - 1 until it either finds f or reaches the bottom floor. 

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
The while loop will continue n number of times, so as n increases the amount of time will increase linearly.


b) O(n)
The function will be linear because the for loop will run through the range depending on n and the while loop will only run some of the time. 


c) O(n^2)
The function is quadratic because it recusively calls itself n times.

## Exercise II

Start at the half way point of the building and drop an egg.
If it breaks, go to the halfway point between the bottom floor and your current floor and repeat.
Otherwise if it does not break, go to the halfway point between your current floor and the top floor and repeat.
If (Floor where egg breaks) - 1 is equal to the floor where the egg doesn't break. 
Then Floor where egg breaks is F.

The runtime complexity is O(log n)

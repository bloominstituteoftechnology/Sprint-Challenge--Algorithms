#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) the code runs n times. We check if the 'a' is less than n**3 and at the same time a is incremented each time by n**2.


b) it takes Square Root(n) times to run the code. The code checks that j < n, and we run j**2 each time.


c) the code runs is same as the bunny count recursively and decrease the count by one.

## Exercise II

We can test by checking if the egg breaks on the middle floor. If it does not break, we can in the middle of current and the higest floor. Otherwise we can check in the middle of the current and the lowest floor. In other words, we always test in the middle. 

high floor = f
low floor = 0
if high floor > low floor:
   middle = high floor / 2
   if breaks(middle)
     high floor = middle
   otherwise
     low floor = middle
high floor = answer



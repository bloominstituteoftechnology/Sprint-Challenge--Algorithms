#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)The answer to this one is logartithmic O(log n) because as the sixe of the input increases the runtime or spave used is will grow at a slightly slower rate.

b)this is quadratic because of the nested loops! These nested for loops mean that for each item in items (the outer loop), we iterate through every item in items (the inner loop). For an input size of n, we have to print n \* n times or n^2 times. O(n^2)

c)The first function is being called recursively n times before reaching base case so its O(n) or linear.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Okay well first pass:
i would want to use a binary search to find the half way point. then at each midpoint drop an egg -
if the egg does NOT break elimate the lesser floors and go to the next halfway point
if the egg DOES break do the same as above but the opposte until you find the floor that breaks the egg...

this makes the time complexity O(logN) logartithmic
beacuse as the the floors increase the longer it will take to get done.

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
o(n)
There is one while loop, which means that the is performing a linear operation based on how large the input that the function is given.

b)
o(n^2)
There is a while loop nested inside a for loop. As i increments, we are running the same operation over and over, until the while loops conditional is met

c)
o(2^n)
This function is recursive, so the runtime will always be based on how deep the recursion goes (which is n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I would try at a midpoint in the building. If the egg breaks, I would go down to the the midpoint between the floor I was at and the bottom floor, and try again. If it didn't break, I would go to the midpoint between the floor I was on and the top, and repeat. I would repeat these steps until I found the floor that is less than floor f. This would be o(log n) runtime, due to me not testing the egg drop on every floor, eliminating linear runtime.
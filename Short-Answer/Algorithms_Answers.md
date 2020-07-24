#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) its a while loop with continue looping n number of times and it has one loop so its O(n)

b) it has a for and while loop so its a O(n) because the for loop runs the whole time while the while loop only runs if j is less than n.

c) because its recursive it calls itself and it also has a if loop so its O(n^2)

## Exercise II

<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->

Start with base case at f floor or higher. and drop the egg.
If the egg breaks go to a floor less then floor f and drop the egg.

Even if it does not break go back to both points and repeat

If you have a floor that the egg ends up breaking and then ends up not breaking, then the floor where the egg breaks is F.

and since its looping twice then it is 0(n^2)


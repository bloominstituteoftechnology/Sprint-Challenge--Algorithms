#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n) because the amount of times the while loop runs is dependent on the value of n.


b) I believe it is something along the lines of O(n^2) because of the nested loop. I know both loop sizes are dependent on the value of n, causing the time complexity to be n raised to a degree, I'm just not too sure on the value of that degree in this block of code.


c) This one should as well be O(n) because you are calling a recursive function until it hits 0 and the thing this code is really dependent on is the value of bunnies

## Exercise II

First you want to find the middle floor and check to see if the egg breaks from the middle floor. Because this is a building and you know floors start at 1 on the bottom and increase +1 for each floor you know that the floors are sorted. Start by cutting your list of floors in half and checking to see if the egg breaks at the middle.
 
    Every time you get to floor that the egg doesn't break you would want to check the floor directly above you to determine if you are at the highest floor. If the floor directly above you breaks the egg then you know you are at the right floor.

    If the egg breaks at the middle then you can cut your list of floors in half again and check to see if the egg breaks at your current floor. If it still breaks, cut in half again. If it does not break you know you went to low and you need to check the upper half of your list. Repeat until you find the correct floor.

    If the egg doesn't break then you know you went too low. You would then implement a similar process to the one above except checking the upper half of your list until you find the correct floor.


I believe this would possibly be O(log n) because you are constantly cutting the list into smaller and smaller halves



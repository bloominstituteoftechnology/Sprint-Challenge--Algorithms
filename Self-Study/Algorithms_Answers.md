# Add your answers to the Algorithms exercises here.

## Exercise I 
# Look at Algoriths_Questions.py to see my notes.

a) O(n) - It iterates through n once. 

b) O(n^3) - It iterates through n three times in the first three loops and the last loop has no input of n making it a constant.

c) O(n) - This is a pattern that calls itself (recursive) which is similar to a for loop and since there is only one for loop iterating bunnies it makes it O(n).

## Exercise II
# Look at Algoriths_Questions.py to see my notes.

Eggs are fragile and without any coverage they will break instantly, thinking in a real world scenerio I would start dropping the egg in ascending order until one of them break which more than likely happen at floor 0. 

Let say that I make an egg container to try to protect as much as possible and want to test how well the container works. Compare to the previous scenario I don't want to start at floor 0 and acend one floor at a time because this is an awesome container and it will take too long until the egg breaks. At this point I would want to start at the middle of the building,_n_//2. If at _n_//2 the egg doesn't break, I will move up one floor at time until it does break. However, if at _n_//2 the egg does break I will move in descending order one floor at a time until the egg stops breaking. If I'm feelling risky, at point _n_//2 if the egg doesn't break I can also go to the middle of the top half of the building and drop the egg and if it doesn't break keep going to the middle of each half until it breaks and vise versa for the bottom half.
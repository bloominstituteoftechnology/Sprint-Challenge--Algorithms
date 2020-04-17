#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n) -- the while loop is iterating starting from 0 and stops the loop when it has accumulated enough value to dissatisfy the condition. -- best case though: if n is a negative number


b)O(log(n)) with base 2 -- the outer for loop that is suppose to be O(n) only runs at the fraction of its range because the while loop inside exponentially increases it's 'j' variable due to 'j *= 2'


c))O(n) -- this is because it is a recursion call and although the only work being done is the conditional check of 'bunnies', the original calling of the function still must wait until we hit the base case. -- it has been recursed 'n' times

## Exercise II

-gets broken whe it is thrown off --- 'f floor'
-'n' floors in the building
-devise a strategy to determine the value of f such that the number of dropped = broken eggs is minimized
1. find the middle of 'n' floors in the building and test the first egg there
2. if the egg breaks, go down to the 'nth' floor that is the midpoint between the 0th floor and midpoint
3. if the egg does not break, go up to the 'nth' floor that is the midpoint between the midpoint and top floor
4. the 'f' floor is located once the opposite outcome of either (2) or (3) occurs.
5. keep repeating (2) and (3) until you experience back to back opposite outcomes (nth floor = breaks but nth-1 floor does not break)

if the egg does break at the middle of 'n' floors you go down to the middle of '0' and 'midpoint of n' floors the egg does not break at this lower midpoint so you go up to the middle between that midpoint and the upper midpoint the egg does break so you can guess between the lower midpoint and that given floor, 'f' is located there continue the process until you narrow it down to essentially 2 (for insanity check) and back to back outcomes are opposite


The runtime complexity is O(log(n)) because we started from the middle and depending on the outcome of the middle, we can exclude a number of floors as either definite 'safety floors' where eggs do not break, or 'dangerous floors', where eggs do break.

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(log n)because that is the Big O of a  while loop and a is constant. 


b) O(n^2) (possibly) because the loops that are nested. An O(n) * O(n) would create O(n^2)


c) I think O(n) because the number of operations doesn't change regardless of n. 

## Exercise II



Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I'm assuming that I would have to sort the floors first because I'm not sure if the floors are in order. I'm thinking that I could try merge sort. So I would have to split the number of floors in half, then split those halves in half, etc until it got to be single numbers and then I could start comparing smaller floor numbers against larger floor numbers and sort. I could use recursion and use a base case that stops it. And maybe if statements that say something like if egg is higher than floor/2 then it breaks. 


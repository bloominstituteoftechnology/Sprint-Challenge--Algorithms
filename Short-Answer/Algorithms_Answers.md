#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) We can treat the while loop the same as a 'for' loop. It will take 'n' times to get through the loop.

b) O(n^2) We have a while loop nested within a 'for' loop. 'For' loops are O(n) while having a nested loop inside is also O(n), and O(n) * O(n) is O(n^2)

c) O(n) The last line is iterative 'return 2 + bunnyEars(bunnies-1)'. We can treat this as a loop.

## Exercise II

'Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.'

O(log(n)) It sounds like a binary search alogorithm is our best option because we are searching for the optimal floor to drop our eggs from. We would start by dropping an egg from the halfway mark, then based on whether it breaks or not we would continue halving the floor count, ie: if we drop it from the halfway mark and it breaks, then we know all floor above the halfway mark can be eliminated, so we would then move halfway down again, and continue the process until we found the optimal location.
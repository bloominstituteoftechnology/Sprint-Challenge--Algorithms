#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) The size of (a) grows proportionally to the size of (n)


b) O(nlog(n)) The outer loop grows proportionally with input size. The inner loop is logn because it is half of whatever the input is.


c) O(n) It contains recursion that is directly affected by the input size.

## Exercise II

I think using a binary tree would be the quickest way to find the solution because this would produce a decent runtime of O(logn). Start at the middle floor between the ground floor and the top floor.

Repeat the following steps until (f) is found:

Drop the egg. If it does not break, move to the middle floor between the current floor and the top floor. If it breaks, move to the middle floor between the current floor and the ground floor. Repeat.

When the highest floor is reached where the egg does not break, that is floor (f).



#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) * O(1) = O(n)


b) O(n) * (O(n) + O(1) + O(1))
   O(n) * (O(2n))
   O(n) * O(n) = O(n^2)


c) Three steps and no loops so: O(3) ?

## Exercise II

new method takes in 1 param (stories)
    set f equal to stories.length -1 so that f is the very top floor and you can only break an egg from the roof, all floors below are safe 
    return f
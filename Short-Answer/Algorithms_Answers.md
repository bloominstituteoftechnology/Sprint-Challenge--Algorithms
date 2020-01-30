#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n); because the n^3 and the n^2 reduce to n


b)
O(n log n); because the j < n is a log n function but only until j meets n; after that, it is only the n iterating with no j


c)
O(n); because although it is a recursive function, the number of operations grows linearly with the number input data (bunnies to ears)
Correct

## Exercise II


Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off
 floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the
  value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

First, go to the middle floor (1st middle). Drop an egg. If it breaks, go lower to the middle floor (2nd middle) in
between the initial middle floor (1st middle) and the ground floor.Drop an egg, if it breaks, go again to the middle
floor (3rd middle) but this time between the second middle floor (2nd middle) and the ground floor. If it does not
break,go up to the floor in the middle of the second middle floor (2nd middle) and the third middle floor (3rd middle).
Continue this process until we reach the highest floor that the egg will not break on (which we would narrow down by
the above process and eventually find the cutoff floor where the egg survives below the cutoff and the egg breaks
above the cutoff).
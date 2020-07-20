#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)It is on because it is not dependent to the size of "n"


b)It is  O(n^2) due to the requirement to loop it twice


c)It is a recursive call on each item so it should be O(n)

## Exercise II
// It is very important to find the midpoint first
// If egg never brek, the upper half should be checked; Add +1 and iterate until reaching floor returns on egg breaks
//Else if egg breaks, the lower half should be checked; Reduce by -1 until reaching a floor that returns that the egg never break.
//Based upon the findings, we can determine the highest floor where the egg never breaks and the lowest floor where it breaks.
//Runtime = O(log n)
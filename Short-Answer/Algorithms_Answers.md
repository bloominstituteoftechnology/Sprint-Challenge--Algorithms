#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    It's O(n) because the a value increases by a constant n^2 after every iteration, and n^3/n^2 is n. 
b)
    It's O(n*log n). Outer loop runs n times, inner loop has a factor increase of *2, so 
    it log base 2 of n is equal to j. iteration runs j times which is log2(n). 
c)  
    This is O(n) because it goes down by 1 from n (bunny ears) until it reaches 0, then it goes back up to provide the answer. So it's basically O(2*n) which boils down to O(n)

## Exercise II

start from the bottom floor and go up a floor and drop an egg until one breaks. the floor that that you drop an egg from where it breaks is f. this is O(1) because the location of f is not determined by the input n, it's basically a floor that eggs just happen to break from if it's dropped from there, so it's 
like an experiment that isn't dependent on the input. 

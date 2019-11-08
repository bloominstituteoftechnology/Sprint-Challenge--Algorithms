#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)a=0 //O(1) single operation
while(a<n*n*n): //O(n^3) time for loop will cube as input increases; e.g., n=2, 8 steps, n=3, 27 steps, etc
a=a+n\*n //single operation (basic math for numbers < 2^64) O(1)

//O(1) + O(1)\*O(n^3) = O(n^3)

b)sum = 0 //O(1)
for i in range(n): //O(n)
j=1 //O(1)
while j < n: //O(n)
j\*=2 //O(1)
sum += 1 //O(1)

//O(n)_O(1)_(O(n)\*O(2)) = O(n^2)

c)def bunnyEars(bunnies):
if bunnies == 0: //Comparison O(1)
return 0 O(1) //will happen once per function call, since bunnies can only equal zero once per FC
return 2 + bunnyEars(bunnies-1) O(1) to return, but will recursively call bunnyEars n=bunnies times, so O(n)

O(n) _ O(1) _ O(1) = O(n)

## Exercise II

//use binary search strategy
let f = n/2 //i is (n/2)th floor
while(n>0):
drop egg from f:
if breaks:
f = f/2 //too high, so half interval from bottom to f
  
 elif not breaks:
dropEgg(f+1): //not breaking here, see if breaks one floor above - if so, we found f
if breaks:  
 return f

            else:i = (i+((n-i)/2))th  //too low, so half interval from nth                           floor (highest) to i

n=n/2 //each step halves the possibilities, so we halve the number
remaining required steps

This should run in O(log n) time, since we halve number of inputs to process at each step.

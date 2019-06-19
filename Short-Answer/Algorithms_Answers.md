Add your answers to the Algorithms exercises here.

## Exercise I

a) Linear O(n):
one loop
while (a < this), a will = that
Not going to be as straight forward as constant bc you're still iterating

b) Quadratic O(n^4):
The number of operations is going to be big.
It has multiple nested loops
Each of the 4 for loops has running time of O(n)
O(n) _ O(n) _ O(n) \ \* O(n) == O(n^4)

c) Linear O(n):
There is recursion
One loop
if bunnies == 0 return bunnies, else return 'that'
This algorithm tells you exactly what to return (kinda like (a) seen above)
Function runs "n" times according to the number of "bunnies" given since it's a recursive iteration

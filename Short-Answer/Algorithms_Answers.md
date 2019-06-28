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

## Exercise II

n == num of stories.
If you cut that in half and start at the middle index (n/2) you will go up or down depending on the egg breaks after being tossed from that floor.

num_eggs == plenty, unlimited throws

f == floor number in order

Binary Search is characteristic of finding the middle index, and giving a solution runtime of O(logn). This could be faster than throwing an egg from the first floor, and moving higher and higher, given that the egg doesn't break on the first go around.

Basically,

1. You would take your list and (find middle floor).
2. Throw egg from middle floor.

- If egg does not break, (ignore floors below) meaning you have to go to a higher floor.
- If egg breaks, (ignore floors above) meaning you need a lower floor

3. Repeat 1 & 2.
4. Once you find where egg breaks next does not you have found _f_ floor.

Add your answers to the Algorithms exercises here.

a) O(n^3)

Line 9 is a single operation and line 10 is a loop the length of n*n*n or n^3 and inside it is a single operation. so we have 1 + 1(n^3). We can drop the leading multiplicative and the smaller additive leaving us with 0(n^3). 

b) O(n^4)

We can ignore line 15 because we know the nested for loops will create a larger Big O and we will end up dropping the other addition. Each of the for loops has a length of n so with 4 nested loops that is O(n^4)

c) 
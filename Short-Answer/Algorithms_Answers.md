Add your answers to the Algorithms exercises here.

a) O(n)

b) O(n^3)

c) O(n)

Exercise 2:

We could assume that the building would equal 'n'
We shall say that the exact floor of the building will equal 'f' 

I would personally attempt a 'for loop' on this problem, checking the length of floors in 'n', moving in reverse order. 

 example: for f in range(len(n) - 1):

I would then need to know at which floor the egg will not break. Once I have this piece of data, I can run a conditional statement and ask, "if the building floor is greater than the 'safeFloor' for the egg, we can safely assume the egg will break. 

example: if f > safeFloor:
           egg = broken 
           return f

This is a very crude example but I believe it would work with enough data. 

 runtime = O(n)
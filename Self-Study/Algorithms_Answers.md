Add your answers to the Algorithms exercises here.

1. 
 a) The runtime is 0(n)
    a=0                     runs one time O(1)
    while (a < n * n * n)   iterates once from 0 to n^3 O(n)
    a = a + n * n           runs once O(1)
    
    O(1) * O(n) *O(1) = O(n)

 b) The runtime is O(n^4)
    
    there are 3 for loops nested inside a abse for loop, each equaling the runtime of  O(n).  O(n) * O(n) * O(n) * O(n) *  = O(n^4)

 c) With recursion in the bunnyEars function, we loop through the input -1 each iteration. 
  So the runtime is O(n)

    
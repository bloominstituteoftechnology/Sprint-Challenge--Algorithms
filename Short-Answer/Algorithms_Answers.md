Add your answers to the Algorithms exercises here.

a) Linear O(n):
       one loop
       while (a < this), a = that
       Not as straight forward as constant, you're still iterating
b) Quadratic O(n^4):
       The number of operations is large.
       Multiple nested loops
       O(n) * O(n) * O(n) * O(n) == O(n^4)
c) Linear O(n):
       There's some recursion going on
       One loop
       if bunnies == 0 return bunnies, else return "that"
       The algorithm tells you explicitly what to return, similar to a)
       
           
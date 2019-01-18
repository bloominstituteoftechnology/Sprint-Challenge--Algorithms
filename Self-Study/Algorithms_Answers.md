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


2. ## use a binary search 
   ## create drop variable and base cases for no drops and floors
   ## find mid floor level which will be my floors //2
   ## if egg breaks at mid floor, drop again from floor //2
   ## if egg doesn't break, drop again at mid floor + midfloor //2
   

eggDrops( eggs, floors ):
    if floors == 0 or floors == 1:
        retrun floors
    
    if eggs == 1: return floors

    
    midfloor == floors //2

    if egg_breaks at midfloor:
         midfloor = midfloor //2
    
    if egg_survives at midfloor:
        midfloor = midfloor + midfloor //2

I am going to the halfway mark and dropping the egg. If it breaks, I go halfway down again and drop it. if it survives, go up halfway from the previous drop and see if it breaks, or repeat the first process if it breaks. I should be able to get this in ~ 10 tries, though i may break a few eggs. I don't optimize eggs survived, but number of eggs dropped. 
    

    



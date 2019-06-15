Add your answers to the Algorithms exercises here.


1) O(n) - I believe this to be true because the amount of cycles the while loop will make depends on the
          size of 'n'. 

2) 0(1) + (0 (n) * (0(1) + (0(n) * (0(1) + (0(n) * (0(1) + (0(1) * (0(1) + 0(1))))))

   Solution = O(n^3)


3) Solution = O(n)

   I arrived at this solution due to the fact that we are dealing with a recursive operation that is repeatedly calling itself, until it eventually reaches 0. The amount of cycles is determined on n's value. 


Exercise 2:

   A proper blueprint for this problem can be acheived with a simple loop. I'm going to use a 'while loop' for this example, due to it's true or false nature. I would apply two variables to begin -

   floor = 0
   brokenEgg = false

   then i'd apply my while loop while testing the condition of the egg -

   while brokenEgg == false: 

   I would then initiate the process and my first condition would consider if the egg breaks -

   if brokenEgg == true:
     return floor
   else: 
     repeat the process and floor += 1

  We'd continue to go up a floor each time until we reach the floor that returns brokenEgg = true

  Solution = O(n)


#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I


a)  a = 0
    while (a < n * n * n):  # the loop is based on n*n*n => O(n^3)
      a = a + n * n         # this makes loop go faster by n*n, we do multipliply first from PEMDAS
                        # the next while loop should see a + n * n < n * n * n
                        # dividing out the n*n results in a < n    
                        OVERALL complexity is => O(n)


b)  sum = 0                 # assignment O(1)
    for i in range(n):      # loop n times  O(n)    
      j = 1                 # assignment O(1)
      while j < n:          # test condition depends on how fast j will increment to get to n
        j *= 2              # assignment O(1)
        sum += 1            # assignment O(1)

                    Regardless of while loop, for loop will run n times
                    OVERALL  complexity is => O(n)

c)
 def bunnyEars(bunnies):  # let bunnies be n
      if bunnies == 0:      
        return 0        

      return 2 + bunnyEars(bunnies-1)   # returns O(1) + O(n-1)
                OVERALL complexity reduces to O(n)
                    


## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

ASSUMING all eggs break the same way....
A basic approach would be a linear search with O(n) complexity and you might use alot of eggs to get answer

A better approach would be like a binary search using midpoints
1) Set up list of of length n for nuber of floors
2) Find midpoint from lowest floor to highest floor
3) Divide into halves, upper floors & lower floors
4) Test out midpoint to see if egg breaks
5) IF eggs breaks: repeat steps 2-5 using lowest half
    OR
   IF egg doesn't break, repeat steps 2-5 on upper half
6) When finally down to 2 floors, the floor where it breaks points to floor where it should not break   



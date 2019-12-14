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



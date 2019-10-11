#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)   a = 0      0(1)
    while (a < n * n * n):      0(n * n * n) => 0(n ^ 3)
      a = a + n * n         0(1)

     Answer =>  0(1) * 0(n ^ 3) => 0(n ^ 3) (Big O)
     If n == 0, runtime will be 0(1)

b)   sum = 0    0(1)
    for i in range(n):      0(n)
      j = 1        0(1)
      while j < n:      0(n)
        j *= 2      0(2) => 0(1)
        sum += 1    0(1)

Answer => 0(1) * 0(n) * 0(1) * 0(n) * 0(1) * 0(1)  => 0(n^2) Big (0)
     If n == 0, runtime will be 0(1)



c)   def bunnyEars(bunnies):    0(1)
      if bunnies == 0:      0(1)
        return 0        0(1)

      return 2 + bunnyEars(bunnies-1)  => 0(n)

Answer => 0(1) * 0(1) * 0(1) * 0(n)  => 0(n)
     


## Exercise II

Get the no of floors => n = total no of floors
Get the current floor => f = current floor
Get the egg dropped => egg = egg dropped

Get the middle floor => middle = n//2

1. Drop the egg from the middle floor
2. If it breaks, it's too high, eliminate the floors above it and work with the floors below 
3. If it doesn't break, it's too low, eliminate the floors below it and work with the floors above
4. Then find the middle floor in the remaining floors and repeat step 1 till you find f

Big O of the algorithm which uses binary search 0(log n)
   


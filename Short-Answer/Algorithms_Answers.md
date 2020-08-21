#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) As n increases in size, the number of loops will increase proportionately, thus the runtime for this pseudocode snippet will be linear O(n).

    a = 0
    while (a < n * n * n): # increasing n
        a = a + n * n # a increases linearly with increasing n



    for n = 1 and a = 0:
    0 < 1^3 = 0 < 1 : a = 0 + 1 * 1 = 1 (1 run)

    for n = 2 and a = 0:
    0 < 2^3 = 0 < 8 : a = 0 + 2 * 2 = 4, a = 4 + 2 * 2 = 8 (2 runs)

    for n = 3 and a = 0:                                            
    0 < 3^3 = 0 < 27 : a = 0 + 3 * 3 = 9, 9 + 3 * 3 = 18, 18 + 3 * 3 = 27 (3 runs)   
    
    for n = 4 and a = 0:
    0 < 4^3 = 0 < 64 : a = 0 + 4 * 4 = 16, 16 + 4 * 4 = 32, 32 + 4 * 4 = 48, 48 + 4 * 4 = 64 (4 runs)

    for n = 5 and a = 0
    0 < 5^3 = 0 < 125 : a = 0 + 5 * 5 = 25, 25 + 5 * 5 = 50, 50 + 5 * 5 = 75, 75 + 5 * 5 = 100, 100 + 5 * 5 = 125 (5 runs)

    for n = 6 and a = 0
    0 < 6^3 = 0 < 216 : a = 0 + 6 * 6 = 36, 72, 108, 144, 180, 216 (6 runs)
    -----------------------------------------------------------------------------------------------------------------------------


b) As n increases in size, the number of loops will increase logarithmically linearly, thus the runtime for this pseudocode snipped will be log-linear O(nlogn)

  sum = 0
  for i in range(n): ### This loop runs proportionate to increasing n (O(n)) ###
    j = 1
    while j < n: ### This loop starts increasing linearly with the for loop, then begins a gradual log-linear increase ###
      j *= 2
      sum += 1


    For the definition:
    def problem_b(n):
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += 1
        j = 1
        while j < n:
        j *= 2
        sum2 += 1
    return sum1, sum2

    The following is true:

    problem_b(0) = (0, 0)        problem_b(1) = (1, 0)            problem_b(2) = (2, 2)
    problem_b(3) = (3, 6)        problem_b(4) = (4, 8)            problem_b(5) = (5, 15)
    problem_b(6) = (6, 18)       problem_b(7) = (7, 21)           problem_b(8) = (8, 24)
    problem_b(9) = (9, 36)       problem_b(10) = (10, 40)

    -----------------------------------------------------------------------------------------------------------------------------

c) This pseudocode function must perform one, and only one operation when taking in the parameter (number of bunnies), but runs recursively for every value of bunnies. Because of this, the runtime is linear O(n)

def bunnyEars(bunnies): # input parameter is bunnies
      if bunnies == 0: # check if bunnies is 0
        return 0

      return 2 + bunnyEars(bunnies-1) # if bunnies is not 0, return 2 + number of bunnies; if there are more than 1 bunnies, this will run the function again recursively



for bunnies = 0             for bunnies = 0                          for bunnies = 3
return = 0                  return 2 + bunnyEars(bunnies-1) = 2      return 2 + bunnyEars(bunnies-1) = 4
total runs = 1              total runs = 1                           total runs = 1

for bunnies = 500
return 2 + bunnyEars(bunnies-1) = 1000
total runs = 1


## Exercise II

We know that we have a building of n stories. We also know that an egg dropped starting at a certain floor (f) will break on that floor and all others above it. We are being asked to determine f so that dropped + broken eggs is minimized. 

In this case we can use a binary search method that would allow us to hone in on our target floor quickly and efficiently.:
    for parameters n (height of building) and f (target floor):
        move to the midpoint of the building: midpoint = n // 2
        check if midpoint == f (our target floor):
            if yes return midpoint
        elif check if midpoint > f (our egg broke when dropped from the floor)
            if yes reset midpoint to be midpoint // 2
        elif check if midpoint < f (our egg did not break when dropped from the floor)
            if yes set midpoint to (n * 3/4)
        loop through these until we find our target floor

The binary search method gives us a big O notation of logarithmic O(logn)
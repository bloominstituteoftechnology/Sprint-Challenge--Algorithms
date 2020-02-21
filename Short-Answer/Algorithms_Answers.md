#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
``` python
a = 0
while (a < n * n * n):
    a = a + n * n
```

Answer: O(n). Each iteration adds n^2 to a. Adding n^2 n times is equivalent to n^3, so the number of iterations is equal to n in positive, >1 cases. Note that the algorithm will run only a single time if n<=1 as n^2 will be >= n^3, but runtime analysis is based on the worst-case scenario.

b)
```
sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1
```

Answer: O(nlog(n)) (base 2). The for-loop will run n times, and each time, the while loop will run log(n) (base 2) times, rounded up. Multiply those together and you get nlog(n). Note that negative or zero values for n will result in the loop not being executed, and non-integer values will result in an error.


c)
```
def bunnyEars(bunnies):
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)
```

Answer: O(n). In the domain of nonnegative integers, the function will recurse n times. Otherwise it will run forever.


## Exercise II


Since a broken egg is twice as "costly" as a dropped but unbroken one, we want to weight our algorithm to favor lower floors. The standard algorithm is to start halfway up, and then keep splitting the remaining distance in half, but to adjust to the special conditions, we instead split the remaining distance into one lower third and a higher two-thirds. This means that with every split, we have a 2/3 chance to gain a lesser amount of information, and 1/3 to gain twice as much information at twice the cost. This algorithm runs at log(n) speed, which is the same as the naive algorithm, but it should have a lower coefficient.


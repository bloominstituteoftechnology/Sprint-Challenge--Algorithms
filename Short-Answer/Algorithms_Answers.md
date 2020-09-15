#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This appears to be a linear runtime as only one operation if being performed and there are no nested loops.

b)
The for loop alone would make this a linear runtime, there is an nested loop, but that loop willl not run the entire length of n making this runtime 0(n log n)

c)
This is a linear runtime. It is a simple loop that  does 1 operation per index.

## Exercise II

1. The best approach I guess would be finding the middle floor and foolishly chucking an egg off. If it breaks we find half the remaining floors and try again, if it does not break we go up a floor until it does an repeat the process.

So n will be max floors.  bottom will be 0 obv and mid will be n // 2. (Floor division. Get it?)

First We Drop it off the middle floor. 

    If it breaks we will set middle to middle // 2 and repeat the process until the egg does not break
        
    Else we will set middle to middle + n // 2 and repeat the process

         If it breaks we will set middle to middle // 2 and repeat the process until the egg does not break
        
        Else we will set middle to middle + n // 2 and repeat the process



IF you have really strong eggs and had to chuck an eg off of every floor your worst case runtime would be linear.


#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n), Reasoning:
    Multiplication is nothing but addition n times.
    n * n is the same as
    n + n-1(n)
    The loop will only need to loop n times before coming to a conclusion. 


b) O(n^2) quadratic. It is looping n times n as it keeps resetting j:
    Every loop will loop for j O(n/2) times. But as it is still linear, we call that O(n) still.
    So outer loop O(n) will loop O(n) times = O(n^2)


c) O(n) even though we're doing recursion, it still requires we create a recursive
    stack of size n, as we're linearly recursively diminishing the size of the passed
    in n by just 1 (n-1)

## Exercise II

Binary search. O(log n).
    We could go up floors by one, but that means that we potentially
    will waste f eggs.
    If instead, we use binary search logic, we will only, worst case scenario,
    waste log f eggs.
    
    Travel to mid floor
        if breaks, travel to mid point between floor and  current floor
            repeat
        if doesn't break, travel to mid point between current floor and max floor
            repeat
    # I'd also like to point out that realistically, we could reach a mid
    floor that is only 1 floor off, so we'd just need to subtract one
        if no more floors to divide:
            if  breaks:
                return f - 1
            else:
                return f
            
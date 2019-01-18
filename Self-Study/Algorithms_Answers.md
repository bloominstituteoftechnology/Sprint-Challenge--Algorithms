Add your answers to the Algorithms exercises here.

1.)
    a.) This algorithm is actually pretty effecient (O(n)) because you would only have
    to run a few calculations to get to the end.
    
    b.) Even though this function is very simple and does one thing, with a large number it could
    be bottlenecked because it is an O(n^4) function.
    
    c.) This function will go quickly for small numbers and seem really efficient but getting into
    bigger numbers you will reach a stack limit because of the amount of the recursion calls
    
    Exercise II :
    n = number of floors
    f = number at which eggs will break
    
    1.) I would take n and divide by 2 and set that to f at the start of the function
    2.) Test the egg to see if it would break at that level
    3.) If it does break subtract 1 from f and test until the egg doesn't break and keep f as that value
    3b.) If it doesn't break with the initial value of f add 1 to f until it does break
        and set f to -1 at the point that it did break
    4.) return f
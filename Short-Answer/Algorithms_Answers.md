##Exercise One: 

a.)
    O(1)+ O(n) * O(1)
    Big O = O(n)

b.)
    Simplified by removing O( )
    1 + (n * (1 + (n * (1 + (n * (1 + (1 * (1 +1))))))
    Big O = O(n^3)

c.)
    This function is recursive and will be called n times making it linear
    Big O = O(n)

##Exercise Two:

I would basically run a binary search on the number of floors and start with the middle floor. we check if f is broken and f-1 is not than we return f else we would run checks to see if f is not broken split from f becomes the starting point and we half the remaining the top portion of the building if f is broken and f -1 is broken the bottom half of the building becomes the area we work with. 

O(log(n))
    

  

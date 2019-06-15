Add your answers to the Algorithms exercises here.

1)
    a) O(n^3)

Line 9 is a single operation and line 10 is a loop the length of n*n*n or n^3 and inside it is a single operation. so we have 1 + 1(n^3). We can drop the leading multiplicative and the smaller additive leaving us with 0(n^3). 

    b) O(n^4)

We can ignore line 15 because we know the nested for loops will create a larger Big O and we will end up dropping the other addition. Each of the for loops has a length of n so with 4 nested loops that is O(n^4)

    c) 
2)

Pseudocode for problem:

    def eggDropped(f)
        if egg is broken:
            return True
        else :
            return False

    start = math.floor(len(n)/2)
    if eggDropped(start):
        for i in range(start, 0, -1):
            if eggDropped(i) == False :
                return i+1
    else :
        for i in range(start, len(n-1)):
            if eggDropped(i) :
                return i

Runtime Complexity:

O(n)

The eggDropped function is O(1) and each for loop is O(n) so I believe my runtime complexity is O(n)
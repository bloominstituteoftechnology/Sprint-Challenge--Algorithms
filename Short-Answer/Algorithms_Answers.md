Add your answers to the Algorithms exercises here.


## Exercise I

a) Linear O(n):
       One loop.
       while (a < this), a = that
       Not as straight forward as constant, you're still iterating.
b) Quadratic O(n^3):
       The number of operations is large.
       Multiple nested loops.
       O(n) * O(n) * O(n) * (last loop not dependent on n) == O(n^3)
c) Linear O(n):
       There's some recursion going on.
       One loop.
       if bunnies == 0 return bunnies, else return "that"
       The algorithm tells you explicitly what to return, similar to a).
       Models the Nth Fibonacci problem.
       

## Exercise II

n == num of stories, if you cut that in half and start at the middle index, n/2, you can either go up or down after that depending if the egg breaks after being thrown from that floor. Since the floors are sorted (in order), this will work

num_eggs == plenty, so you have as many throws as you need, essentially

f == floor number 

If i refer to what I learned about big O, Binary Search is charactaristic of finding the middle index, giving this solution a runtime of O(logn). This could potentially be faster than throwing an egg from the first floor and going up from there, unless you're lucky and the egg breaks on the first floor.

low = 0
high = len(n)-1
while low <= high:
    middle = n/2
    if f < n[middle]:
        high = middle-1
    elif f > n[middle]:
    low = middle+1
else:
    return middle
return -1


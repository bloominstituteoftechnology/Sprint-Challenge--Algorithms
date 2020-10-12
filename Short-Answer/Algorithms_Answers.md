#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). This while loop runs n times. It gorws at n(2) and the while loop runs at n(3). n(3)-n(2) = n


b)O(nlogN) - grows faster than O(n) with two loops but is not O(n^2) since j doubles on the inner lloop.


c) O(n) single recursive call.

## Exercise II
Start at middle floor, if the egg breaks go to n/2 position. If egg breaks go down half of current position and try again. If it doesn't break then go up half of current position until zero in on maximum floor. The runtime is O(logn) each time we go through half floors we need to check. 

def egg_toss([n]): 
    middle = len(n)//2 
    if n[middle] == 'Egg broken': 
        egg_toss(n[:middle]) 
    elif n[middle] == 'Egg not broken': 
        egg_toss(n[middle:])


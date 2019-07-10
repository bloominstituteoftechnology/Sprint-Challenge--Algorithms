Add your answers to the Algorithms exercises here.

Exercise 1
a) O(n)
b) O(n^n)
c) O(n^2)

Exercise 2

def maxSafeFloor(n) 
dropfloor = 1
brokenEgg = false

While (broken == false AND dropfloor <= n):
    drop egg from dropfloor
    if egg breaks:
        brokenEgg = true
    else:
        dropfloor =+ 1

if dropfloor == 1
    return 0
elif dropfloor > n:
    return 'Egg never broke'
else:
    return dropfloor
Add your answers to the Algorithms exercises here.
#Exercise I
a) setting a = 0 is O(1), a < n * n * n is O(n^2), a + n * n is O(n)
so it would be O(n^2) because it's the largest of the three

b) sum = 0 and sum += 1 would be O(1), we have three nested loop with n so it would be O(n*3)

c) This looks like a recursion I think it's O(n) because n is linear


#Exercise II

We have a building with story = n , if x > f, eggs will break more. x < f eggs would break less


use binary search sort

def broken_eggs(n, f):
    n is an array of the building
    n = [1, 2, 3, 4, 5, 6, 7]
    x = n / 2 to choose mid point
    for i in range(len(n)):
        if n[i] < f:
        
Add your answers to the Algorithms exercises here.

1.
a) O(n)
We have one loop running which is O(n), within that loop is an 0(1) operation, 0(n)*0(1) is simplified to 0(n)
b) O(n^4)
There are 4 loops nested within each other O(n)*O(n)*O(n)*O(n) is O(n^4)
c) O(n)
This is a recursive functions which operates the same as a loop giving it an O(n) time complexity

2. Find out which floor is the middle floor. Then, drop an egg from that floor. If the egg breaks, then find the midpoint between that floor and the floor below it, ignoring all floors above where the egg was initially dropped. Drop the egg from that midpoint and repeat the process, until theres only two floors left, then whichever floor the egg breaks from is value f. Whenever the egg doesnt break, instead of ignoring the top floors and finding the new midpoint from the bottom floors, instead ignore all floors below the point from where the egg was dropped and find a new midpoint from that point to the upper-most floor, repeat process using this conditional and the instructions below to find the value of f the fastest.

Add your answers to the Algorithms exercises here.

a.) O(log n) because even though we are multiply n^3 on our while loop, we are changing a (which is what our while loop depends on to break out of) by adding a + n^2
thus giving us a power of 2 solution and making it a log problem.

b.) I believe the correct answer is O(n^4). Our first loop is O(n) our second loop is O(n+1) because we are adding one more than our previous loop and it does this again

c.) O(n), the 2 + has no bearing on the amount of bunnies there are. the (bunnies -1) is what we are looking at to break out of our recursive function call and since that subtracts 1 everytime, best case is O(1) worst case would be O(n)

Excercise 2 -> create an anchor that find the middle floor and sets it to _f_ then check if throwing an egg off breaks it. If it does, then we need to find the middle floor of the left side (lower floors) and test again. In the case the egg DOESNT break, we can do the same to the right side and check if the egg doesnt break still. If it does break on the right check, then we go left. We can repeat this process until we find the exact floor which an egg breaks or doesnt break.

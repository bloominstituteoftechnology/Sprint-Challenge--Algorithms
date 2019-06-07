Exercise I

a) O(n); For n = 1, 1^3 = 1, and the while loop terminates after one iteration when a = 1^2, which is 1. For n = 2, 2^3 = 8, and the while loop terminates after two iterations: 0 + 2^2 = 4, then 4 + 2^2 = 8. Similarly, when n = 3, the while loop terminates after three iterations when a = 3^3, which is 27. Each iteration adds 3^2, which is 9. 27 / 9 = 3. The iterations are increasing linearly as n increases, so the time complexity is O(n). More specifically it is O(n^3 / n^2), which simplifies to O(n).

b) O(n^3); The for i loop loops n times, the for j loop loops n-1 times, the for k loop loops n-2 times, and the for l loop loops a constant number of times. The time complexity is O(9*n*(n-1)*(n-2)), which simplifies to O(n^3).

c) O(n): As n increases by one, the number of times the function is called increases by one.

Exercise II

function minimizeNumberOfDroppedEggs(n, f):
    return f

This function is of O(1) time complexity. Returning the floor at which eggs are thrown instead of dropped minimizes the number of dropped eggs to 0.
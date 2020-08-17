#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity is O(n). This is because with each iteration of the while loop, 'a' increases by 'n * n', so after 'n' iterations 'a' will be equal to 'n * (n * n)' which matches the while loop's conditional check of 'a < n * n * n'.

b) The runtime complexity is O(n*log(n)). This is because there are nested loops: the outer 'for' loop will run 'n' times, and the inner 'while' loop will run log(n) times. The inner loop has a log(n) time complexity because the value of 'j' doubles with each iteration, so 'j' will increase quadradically and only take log(n) iterations to reach the value of 'n'.

c) The runtime complexity is O(n). This is because the function is recursive and will call itself 'n' times. When it hits its base case, the function will backtrack through all 'n' function calls, adding '2' to the return value each time. Since adding '2' to another value is a constant time operation, and it is done 'n' times, the final runtime complexity is O(n).

## Exercise II



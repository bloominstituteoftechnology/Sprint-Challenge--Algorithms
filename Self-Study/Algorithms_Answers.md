Exercise I

a: This psuedocode has a runtime of O(n). Since "a" grows by n^2 every time the loop runs, it only takes n times to be equal to n^3.

b: The first loop runs n times, while the second and third loops run less than n times due to running on a range with an incremented start. The fourth loop will always run greater than n times because of the range it's given. The runtime is at least O(n^2).

c: The runtime is O(n), nothing increases n so it will only run n times.
#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) the amount of times the loop will run depends on the value of n.

b) O(n log n) The outer loop would have a runtime of O(n) because it is dependant on value of n, which is linear. The inner loop will have a runtime complexity of O(log n) because the iterator (j) is incremented by doubling its value with each successive loop. This doubling would cause the loop to run in half the range of n. The inner loop denotes a runtime complexity of O(log n).

c) O(n). The function will run in relation of value of n.

## Exercise II

Take the middle point of the building: if the egg gets broken take the middle of the floors bellow if not take the middle floor of the floors above. Repeat untill one is left.

Runtime: O(log n)

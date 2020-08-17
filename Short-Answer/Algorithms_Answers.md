#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity is O(n) since the while loop runtime will increase in a manner that is proportional to the size of input n. This is indicative of linear runtime.


b) The runtime of this would be O(n log (n)). The outer for loop would have a runtime of O(n) because it is dependent on the linear relationship of the input size of n. The inner while loop will have a runtime complexity of O(log n) due to the fact that `j` is incremented by doubling its value with each loop. The doubling would cause the loop to run in half the range of n. 


c) The runtime complexity is O(n). The only computation occuring is reduciing the number of bunnies by one with each recursive call. 

## Exercise II

For this question, I would use a recursive binary search function to find the value of f such that the number of dropped + broken eggs is minimized.

def determine_egg_break(n):
    list_of_floors = [0, 1, ..., n]
         
next steps:
- choose middle point, and drop an egg
- if the egg breaks, the function will recurse using the lower half of the list
- if the egg doesn’t break, the function will recurse using the upper half of the list

Runtime complexity: O(log n) 
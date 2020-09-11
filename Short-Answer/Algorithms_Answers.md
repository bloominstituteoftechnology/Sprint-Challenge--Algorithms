#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Runtime Complexity: O(1 + (n^3 * 1)) -> O(log n)

Justification: Since a is increasing by n^2 & being compared to n^3, it will reach the target much quicker than a standard n^3 method would. For example, if n was 3, it would only take 2 passes before the block exited as a would equal 9 after the first round and 36 after the second which is greater than 27.

b)
Runtime Complexity: O(1 + (n * (1 + log n * (1 + 1)))) -> O(1 + (n * 3 log n)) -> O(n log n)

Justification: This has a runtime complexity of O(n log n) since the outer for loop will continue running until the entire range of n has executed. The inner while loop, however, multiplies j by 2 each time significantly decreasing the amount of times it will be called to increase the sum making that combination n log n.

c)
Runtime Complexity: O((1 * 1) + n) -> O(n)

Justification: Since the method only has a runtime of O(1) outside of the recursive call, it will only need to add to the call stack until n is 0 giving it a runtime complexity of O(n)

## Exercise II
Possible Solution: Use a binary search algorithm to efficiently determine if a guess is too high / low, starting with the middle element. This will eliminate half the options immediately and minimze the number of eggs dropped / broken.

Runtime Complexity: O(1 + 1 + log n * (1 + 1 + 1)) -> O(log n)

Justification: Since we cut the amount of available guess elements in half each time, it will take log n runtime complexity before we find the floor, even if it's the very last guess.

Pseudocode:
def egg_drop(building, floor):
  # Start will full building floors list and set pointers for start and end of list
  low = 0 #O(1)
  high = len(building) - 1 #O(1)

  # While low <= high, loop through elements to find the middle and make that the next guess until f-floor is located
  while low <= high: #O(log n)
    # Find the middle of current range
    mid = (low + high) // 2 #O(1)

    # If building[mid] is the correct floor, return that value
    if building[mid] == floor:
      return building[mid] #O(1)
    
    # If floor is below the mid, eliminate the top half of the list
    if building[mid] > floor:
      high = mid - 1 #O(1)

    # If floor is above the middle, eliminate the bottom half of the list
    if building[mid] < floor:
      low = mid + 1 #O(1)


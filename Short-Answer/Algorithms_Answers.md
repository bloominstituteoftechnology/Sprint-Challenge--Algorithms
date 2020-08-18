#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime for the whole function is O(n^3). For example if n = 2, then this loop will run 8 times (222 = 2^3 = 8); if n = 4, then this loop will run 64 times (444 = 4^3 = 64) This line a = a + n * n is O(1) - no matter how big n is without that while loop this line would have run only once

a)  a = 0
    while (a < n * n * n):
      a = a + n * n

b) For loop has runtime of O(n) While loop has runtime of O(n/2) So general runtime will be O(n^2) => n * n/2 = (n^2)/2. In this case the constant in BigO can be ignored, that's why it's just n^2

b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1


c) The runtime for this function is O(n). No matter how big n is (or how many bunnies there are) it won't run more time. If bunnies = 5, the function will run only 5 times: n = 5 => n - 1 = 4 => n - 1 = 3 => n - 1 = 2 => n - 1 = 1 => 0

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

## Exercise II

The runtime is O(log(n)) Algorithm:

Writing the recursive function with 2 params: n that is the arr of sorted numbers and target when the egg is broken
Dividing the length of an array (n) on 2.
If target (f) is bigger than len(n)//2 then recursively return the same function where first param is second half of the previously given array (arr[len(arr)//2]+1:)
If target (f) is smaller than len(n)//2 then recursively return the same function where first param is first half of the previously given array (arr[:len(arr)//2])
if target (f) is equal return arr[len(arr)//2]

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.


## Exercise II



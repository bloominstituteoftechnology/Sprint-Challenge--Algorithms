#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n) is the answer. When the while loops run 'a' which is initially set to 0. Let's assume that n is 5 and then the first loop will become 25. On the second the a becomes 50. Each loop will take 5 rounds to reach 125 and then breaks the loop.

b)
O(log(n)). We first get n, and the outer loop is going to run 'n' time regardless of what happens in the inner loop. Then in the inner loop, the number 'j' that has to reach the value of 'n' loops which grows. The input of the size of 'n' gets larger, j will catch up to n more quickly relative to the size of the number 'n'.

c)
O(n). As long as there is a return value, the recursion will not run an infinite loop.

## Exercise II

O(log(n))

1. Check the floor that is halway up if it breaks.
2. if it breaks, then take all of the floors from 1 up to the middle floor.
3. if it doesn't break, check the halfway floor between the one. Then, checked the top floor.

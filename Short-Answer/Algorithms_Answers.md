### Exercise 1
a) O(n) 
b) O(n^4)
c) O(1^n)

### Exercise 2
- let n be the number or stories in the building 
- let f be the height at which an egg breaks 
- if n is greater than f then egg is broken, stop wasting egg 
 
- while f is less than n           O(n)
      drop egg                     O(1)
      move up another floor        O(1)


total runtime = O(n)
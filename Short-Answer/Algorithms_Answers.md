Add your answers to the Algorithms exercises here:

# For some reason it automatically changes a lot of the operators to underscores on save... some of them stay preserved

## Also, it re-formats to all be at the same tab width on save as well

a) a = 0 # O(1)
while (a < n \* n \* n): # O(n)
a = a + n \* n # O(n)

// add what happens in sequence, multiply what is in a loop
1 + (n \* n)
// drop the O(1) and multiply the two n's
2n
// drop the coefficient (leading multiplicative constant)

## Answer to a):

Runtime: O(n)

b) sum = 0 # O(1)
for i in range(n): # O(n)
i += 1 O(1)
for j in range(i + 1, n): O(n)
j += 1 O(1)
for k in range(j + 1, n): O(n)
k += 1 O(1)
for l in range(k + 1, 10 + k): O(9)
l += 1 O(1)
sum += 1 O(1)

// add what happens in sequence, multiply what is in a loop
1 + ((n _ 1) _ (n _ 1) _ (n _ 1) _ (9 _ 1 _ 1))
// drop the 1's and constants (9)
(n) _ (n) _ (n)
// do the multiplication

## Answer to b):

Runtime: O(n^3)

c) def bunnyEars(bunnies):
if bunnies == 0:
return 0

       return 2 + bunnyEars(bunnies-1)

## Answer to c):

O(n) - at least that is my best guess based off the lecture material covering recursion run time

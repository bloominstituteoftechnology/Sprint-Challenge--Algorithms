Add your answers to the Algorithms exercises here:

a) a = 0 # O(1)
while (a < n _ n _ n): # O(n)
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
for l in range(k + 1, 10 + k): O(n)
l += 1 O(1)
sum += 1 O(1)

c) def bunnyEars(bunnies):
if bunnies == 0:
return 0

      return 2 + bunnyEars(bunnies-1)

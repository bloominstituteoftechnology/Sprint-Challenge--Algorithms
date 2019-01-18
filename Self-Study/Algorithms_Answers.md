Add your answers to the Algorithms exercises here.

## Exercise I

a) a = 0 `O(1)`
while (a < n _ n _ n) `O(n)
a = a + n \* n

O(n)
if n = 5, it would take 5 iterations for the while loop to break
if n = 10, it would take 10 iterations
double the input, double iterations

b) sum = 0 `O(1)`
for (i = 0; i < n; i++) `O(n)`
for (j = i + 1; j < n; j++) `O(n)`
for (k = j + 1; k < n; k++) `O(n)`
for (l = k + 1; l < 10 + k; l++) `O(n)`
sum++

O(n^4)
Nested loops

c) bunnyEars = function(bunnies) {
if (bunnies == 0) return 0 `O(1)`
return 2 + bunnyEars(bunnies-1) `O(n)`
}

O(n)
Recursion.
bunnyEars = 2
bunnyEars(10 - 1)
2 + (2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2)

## Exercise II

We can take a binary search approach. Go to the half way point of the floors and throw the egg. If it breaks, then we walk down from the middle and do it again. If it doesn't break, go half way up from the middle and throw the egg.
We will repeat that until we find floor f where the egg breaks if it gets thrown off floor f and higher, and wouldn't break if it's thrown off floor f and lower.

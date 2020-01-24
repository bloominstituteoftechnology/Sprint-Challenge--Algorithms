#### Please add your solutionwers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
while loop = O(n)
calculation a = a + n * n constant = O(1)

solution = O(n) * O(1) = O(n)

b)
for loop = O(n)
n is evaluated again in while loop = O(n)

solution = O(n) * O(n) = O(n^2)

c)
the input of n is independent from the function, so constant = O(1)

solution = O(1)

## Exercise II
1. proceed to floor n/2 and drop an egg
2. if broken go to floor between 0 and n/2
3. else if egg sustained go to floor between n/2 and n
4. repeat 2/3 on current floor being the "flight -" if egg is unbroken and the last visited floor being the "flight + " (vice versa if broken) until f is determined

O(log n) : Essentially a binary search and will have a runtime complexity that is much the same.
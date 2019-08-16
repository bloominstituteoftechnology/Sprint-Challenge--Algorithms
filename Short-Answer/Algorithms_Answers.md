Add your answers to the Algorithms exercises here.

Exercise I:
a)  a=0 is                          O(1) and is constant
    while (a < n * n * n):          is determined by how 'a' iterates
    a = a + n * n                   this line defines a's iteration as n^2.

    So, taking a=0, while n increases by a power of 3, the loop will run by a power of 2. This will reduce to n^1 or O(n) and since that is the worst ot least efficient, that is the time complexity.

b) sum = 0                          O(1)
    for i in range(n):              O(n)
        i += 1
    for j in range(i + 1, n):       O(n) * O(n log(n))
        j += 1
    for k in range(j + 1, n):       O(n) * O(n log(n))^2
        k += 1
    for l in range(k + 1, 10 + k):  O(n) * O(n log(n))^2 * O(10n)
        l += 1
        sum += 
        
    Because of the nested loops time complexity would be O(n*n*n*n) or O(n^4)

c)  def bunnyEars(bunnies):
    if bunnies == 0:                O(1)
    return 0                        O(1)

    return 2 + bunnyEars(bunnies-1) O(n)

    This is a recursive function since it calls itself, droping one 'n' per recursion until it reaches the base case. Time complexity = O(n)
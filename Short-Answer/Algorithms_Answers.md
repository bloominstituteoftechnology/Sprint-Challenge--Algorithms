Add your answers to the Algorithms exercises here.


Exercise I

a)
```
a = 0 # --> O(1)
while (a < n * n * n): # --> O(n)
    a = a + n * n # --> O(1)
```
This is an O(n) algorithm. The first line will only happen once, no matter what `n` is equal to. The `while` loop is tricky. Just because it's a loop that depends on `n`, does that give it O(n) time complexity. It does. The amount of times the `while` loop will run is dependant on the input `n`. It is O(n). The last line is also O(1). No matter what the size of `n` is, the line of code will only run once when it is called and will only repeat once the `while` loop starts up again.

b)

```
sum = 0 # --> O(1)
for i in range(n): # --> O(n)
    i += 1 # --> O(1)
    for j in range(i + 1, n): # --> O(n)
        j += 1 # --> O(1)
        for k in range(j + 1, n): # --> O(n)
            k += 1 # --> O(1)
            for l in range(k + 1, 10 + k): # --> O(n)
                l += 1 # --> O(1)
                sum += 1 # --> O(1)
```
Wow this is an expensive algorithm. This is either an O(n ** 4) algorithm. Every time we run through this algorithm, we will run through a `for` loop with 2 nested `for` loops that also scale with the size of `n`. 

The first line of code is O(1) because it will only ever repeat once, it does not scale at all no matter the size of `n`.

The second line is O(n) because the number of times that `for` loop is called scales with the size of `n`.

The third line is O(1) because it will only ever repeat a fixed amount of times (once in this case) inside of the loop, no matter the size of `n`.

The fourth line of code is O(n) because the amount of times the loop is called scales with the size of `n`.

The fifth line is O(1). See the explanation for third line.

The sixth line is O(n). See explanation for the fourth line.

The seventh line is O(1). See explanation for third line.

The eighth line is O(n). This `for` loop will indirectly scale with the size of `n`. This is because `k` will scale with the size of `n` and `l` will scale with the size of `k`, therefore the size of `l` is dependant on the size of `n`. This `for` loop will run more times or less times dependant on the size of `n`.

The next two lines are O(1). See explanation for the third line.

Because we have a `for` loop with three nested `for` loops nested inside of each other, this algorithm has an O(n ** 4) time complexity. In other words, this algorithm's time complexity is O(n*n*n*n). Every one of the `for` loops present in this algorithm is directly or indirectly dependent upon `n` for the amount of times it is going to run.

c)

```
def bunnyEars(bunnies):
    if bunnies == 0: # --> O(1)
        return 0 # --> O(1)

    return 2 + bunnyEars(bunnies-1)O(n)
```
This algorithm has an O(n) time complexity.

The first two lines of code are O(1) because they will only each run a set amount of times and do not scale with the size of input.

The last line of code is O(n) because it starts a recursive loop that runs a certain amount of times that is scaled along with `n`.

Exercise II

`n = 5`
|
|
|
|
|

Add your answers to the Algorithms exercises here.

## Exercise I

```
a)  a = 0 `O(1)`
    while (a < n * n * n)
      a = a + n * n
```

To first analyze the time complexity of this algorithm, let's break this algorithm down:

We have three blocks of code to examine:
1. a = 0
2. while (a < n ^ 3)
3. a = a + n ^ 2

We know that both `a = 0`, and `a = a + n ^ 2` have `O(1)` time complexity because, regardless of how big the input gets, those blocks won't run more than once by themselves.

However, because `a = a + n ^ 2` is inside of another block, a loop in this case, we need to identify the time complexity of the loop in addition to its contents to fully understand the time complexity.

The loop stops iterating when `a` has grown to reach a size of `n ^ 3` or larger. The block inside of the loop increments `a` by `n^2` each iteration.  

Let's take a look at the result of a few examples: 
`n = 1, # of iterations = 1; `, `n = 2, # of iterations = 2`, `n = 3, # of iterations = 3`

We can see a linear time complexity start to appear. 

Mathematically, this also makes sense since `n ^ 3 / n ^ 2 = n`. Essentially, we are going to add 1/nth of our condition to `a` during each iteration. That means that our loop will always run exactly n times!

Time Complexity: O(n)


```
b)  sum = 0
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```
In this algorithm, we have several more blocks of code, but it's easier to understand given that we only ever increment by 1. 

We have six blocks of code to examine:

1. sum = 0
2. for (i = 0; i < n; i++)
3. for (j = i + 1; j < n; j++)
4. for (k = j + 1; k < n; k++)
5. for (l = k + 1; l < 10 + k; l++)
6. sum++

Again, we know that both `sum = 0`, and `sum++` have `O(1)` time complexity because, regardless of how big the input gets, those blocks won't run more than once by themselves.

I wish that I could be more rigorous, but I don't have enough time, so here is a quick breakdown:

1. sum = 0 `O(n)`
2. for (i = 0; i < n; i++)  O(n) 
3. for (j = i + 1; j < n; j++) O(n)
4. for (k = j + 1; k < n; k++) O(n)
5. for (l = k + 1; l < 10 + k; l++) 
6. sum++ `O(n)`

Time complexity: O(n ^ 3)

 
```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```

In this recursive algorithm, we have a function `bunnyEars` that calls itself only if `bunnies` is not equal to `0`.

Because this is recursive, we can essentially write the time complexity as the time complexity of the function that pushes it towards its base case. In this case, that is:
`return 2 + bunnyEars(bunnies - 1)` Which means that, each iteration, bunnies will decrease by 1 until it reaches 0, at which point `0` will be returned. This is a linear relationship.
`return 0`, is of course, `O(1)`.

Time complexity: O(n)
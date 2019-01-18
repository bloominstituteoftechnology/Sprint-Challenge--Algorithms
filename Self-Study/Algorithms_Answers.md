Add your answers to the Algorithms exercises here.
## Exercise I -- Answers
a)   Time complexity  : O(n) as while loop depends on a and n it is `O(n+a)` ignoring constant : `O(n)`

b)   Time complexity  : O(n^4) as four `FOR LOOPS` are there which are going 
                        for (i = 0; i < n; i++) `O(n)`
                            for (j = i + 1; j < n; j++) `O(n-1)`
                                for (k = j + 1; k < n; k++) `O(n-2)`
                                    for (l = k + 1; l < 10 + k; l++) `O(n-3+10)`
    `T = O(n) * O(n-1) * O(n-2) * O(n-3+10)` ignoring all constants it will be :: `O(n^4)`

c)   Time complexity  : O(n)  recursive call

## Exercise II -- Answers


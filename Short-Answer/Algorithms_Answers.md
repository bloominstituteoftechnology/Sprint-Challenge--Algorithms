#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Linear runtime, in the worst case

<div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule:">
<div style="display: inline-block;">
<h3>Original Code</h3>
<pre>
<code class="language-python">a = 0
  while (a < n * n * n):    
    a = a + n * n </code>
</pre>
</div>
<div style="display: inline-block;">
<h3>Justification</h3>
<pre>
<code class="language-python">O(1) <!-- simple variable assignment --->
O(n) <!-- while loop, determined by size of `n`
        since `a` is known to be 0 --->
O(n) <!-- variable assigment again --->
</code></pre>
    </div>
</div>

b) O(n^2) - Quadratic runtime, in the worst case

<div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;">
<div style="display: inline-block;">
<h3>Original Code</h3>
<pre>
<code class="language-python">sum = 0
  for i in range(n):
    j = 1
    while j < n:
      j *= 2
      sum += 1  </code>
</pre>
</div>
<div style="display: inline-block;">
<h3>Justification</h3>
<pre>
<code class="language-python">O(1) <!-- simple variable assignment --->
O(n) <!-- `for loop`, determined by size of `n`
        since `a` is known to be 0 --->
O(1) <!-- simple variable assignment  --->
O(n^2) <!-- nested while loop --->
O(2n) <!-- value is mutliped by 2 -->
O(1) <!-- value is added to by 1 --></code>
</pre>
    </div>
</div>

c) O(n) - Linear runtime, in the worst case

<div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule:">
<div style="display: inline-block;">
<h3>Original Code</h3>
<pre>
<code class="language-python">def bunnyEars(bunnies):
  if bunnies == 0:
    return 0

  return 2 + bunnyEars(bunnies-1)</code>
</pre>
</div>
<div style="display: inline-block;">
<h3>Justification</h3>
<pre>
<code class="language-python"> <!-- funtion declaration, no runtime -->
<!-- `if statement`, no runtime -->  
O(1) <!-- constant runtime -->
O(2 + n) <!-- 2 + call of recursive function, dependent on size of variable --></code>
</pre>
</div>
</div>

## Exercise II
```
Go to the middle floor of the building by dividing `n` by two:
  drop the egg from current floor:
    if the egg does not break
        go halfway up the building (by adding current floor to total floors (n) and dividing sum by two)
        repeat step 2
    if the egg does break
      go up one floor
        drop the egg from current floor
          if the egg breaks
            return current floor minus one as `f`
          if the egg does not break
            go to step 3
```
O(log n) - Logarithmic runtime, in the worst case, because the problem is halved on each pass, making the solution relatively quick to obtain.

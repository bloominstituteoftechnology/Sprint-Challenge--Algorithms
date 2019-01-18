Add your answers to the Algorithms exercises here.

## Exercise I
a)  
If n = 1
while (0 < 1 * 1 * 1) => True
	a = 0 + 1 * 1
	a = 1
while (1 < 1 * 1 * 1) => False

===> For n = 1, we executed 1 loop.

If n = 2
while (0 < 2 * 2 * 2) => True
	a = 0 + 2 * 2
	a = 4
while (4 < 2 * 2 * 2) => True
	a = 4 + 2 * 2
	a = 8
while (8 < 2 * 2 * 2) => False

===> For n = 2, we executed 2 loops.

If n = 3
while (0 < 3 * 3 * 3) => True
	a = 0 + 3 * 3
	a = 9
while (9 < 3 * 3 * 3) => True
	a = 9 + 3 * 3
	a = 18
while (18 < 3 * 3 * 3) => True
	a = 18 + 3 * 3
	a = 27
while (27 < 3 * 3 * 3) => False

===> For n = 3, we executed 3 loops.

====> From the patterns, we can see that as input n increases, the number of loops increases. Therefore, we can assumne that this method depends on input n, so the operation is O(n).



b)  sum = 0
		for (i = 0; i < n; i++)
			for (j = i + 1; j < n; j++)
				for (k = j + 1; k < n; k++)
					for (l = k + 1; l < 10 + k; l++)
						sum++
						
Working backward, starting from sum...
				
sum++ => O(1)

for (l = k + 1; l < 10 + k; l++)
					 ^
===> No matter what k is, l is always done 10 times
===> 10 * O(1) = O(10) ==> O(1)

for (k = j + 1; k < n; k++)
		 ^			^
===> if n = 5000, j = 0
	It would take 4999 operations until k is no longer less than n.
===> if n = 5000, j = 4000
	It would take 999 operations until k is no longer less than n.

====> We can see that as input n increases, the number of operations decreases.
	Operation = n - j - 1
	O(n - j - 1) * O(1) => O(n)
	
for (j = i + 1; j < n; j++)
		 ^			^
===> This loop is similar to the loop above, where it depends on i and n.
	Operation = n - i - 1
	O(n - i - 1) * O(n - j - 1) => O(n^2)
	
for (i = 0; i < n; i++)
				^
===> This loop is similar to the loop above, where it depends on n only.
	Operation = n
	O(n) * O(n - i - 1) * O(n - j - 1) => O(n^3)
	The overall operation is O(n^3).
	


c)  bunnyEars = function(bunnies) {
			if (bunnies == 0) return 0
			return 2 + bunnyEars(bunnies-1)
		}
		
If...
n = 0 => 0
n = 1 => 2 + function(0)
n = 2 => 2 + function(1) => 2 + (2 + f(0))
n = 3 => 2 + function(2) => 2 + (2 + f(1)) => 2 + (2 + f(0))

===> Every time the function is called, we get 1 unit of work.
	As input n increases, the number of operations increases.
	Therefore, this operation is O(n).
	


## Exercise II

-	|-------|									-
|	|		|									|
|	|		|									|
|	|		|			egg broken				|
|	|		|									|	new _f_
|n	|		|	-		-------					|
|	|		|	|								|
|	|		|	| f		egg not broken			|
|	|		|	|								|
_	-----------	-								-


?? Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.??

==> The number of dropped eggs doesn't depend on _f_ or _n_.
	But if we want to minimized the number of broken eggs, and assuming we are in control of _f_, then we want _f_ to be as closed to _n_ as possible. Ideally, _f_ > _n_.
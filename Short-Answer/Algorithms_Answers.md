#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n), loop will take increasingly longer to finish as n increases


b) O(n^2), double loop , maybe considered O(log n)?


c) O(n), recursion will call itself n times

## Exercise II

	# n stories
	# egg breaks if on_floor >= f
	# egg not broken if on_floor < f
	# is problem assuming f is random?

	Assuming f is between floors 2 -> n, I would calculate the middle floor, drop an egg.

	if it breaks calculate a new middle between 0 -> mid, in a loop until it doesnt break anymore

	if the egg does not break, then the new middle should be between mid -> n

	will be able to see if the last floor dropped from didnt break and that floor +1 does, then f has been located, this will be O(log n) runtime since it is a binary search

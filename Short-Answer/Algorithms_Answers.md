#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3)


b) O(n^2)


c) O(n-1)

## Exercise II


def egg_break_search(floors, break_point):
	first = 0
	last = len(floos) - 1
	index = -1
	while (first <= last) and (index == -1):
		mid = (first + last) // 2
		if floors[mid] == break_point:
			index = mid

		else:
			if break_point < floors[mid]:
				last = mid - 1

			else:
				first = mid + 1

	return index

		



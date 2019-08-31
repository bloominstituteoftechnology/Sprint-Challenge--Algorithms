#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) n doesn't get modified, therefore it grows linearly.


b) O(n^2) There are two loops, each with a O(n), therefore they get multiplied together.


c) O(n-1)/ "O(n)" in every recursive call n is subracted by 1. 

## Exercise II
break_points = {}
break_floor = Int

for n in floors:
	if n >= break_floor:
		break_points.update(n = True)
	else:
		break_point.update(n = False)

def egg_break_search(floors, break_points):
	first = 0
	last = len(floors) - 1
	index = -1
	while (first <= last) and (index == -1):
		mid = (first + last) // 2
		if break_points[floors[mid]] == True and break_points[floors[mid - 1]] == False:
			index = mid

		else:
			if break_point[floors[mid]] == False
				last = mid + 1

			else:
				first = mid - 1

	return index

		
This is just a basic implamentation of a binary search. The function take finds the number of floors by taking the first and lanst floor and subtracting them from each other. Then it takes the middle of the floors and drops the egg. If the egg breaks we go to the floor below and check if it breaks. If it doesn't the break break floor is the current floor plus one. If the dropped eg doesn't break then the problem gets re ran with the first floor now the mid + 1. Else the first floor is the mid floor - 1. The problem repeats until the correct floor is returned.

Time Complexity = O(log n) "base 2"


